import pygame
import pyaudio
import numpy as np
import speech_recognition as sr
from Lumen.Core.SpeechHandler import SpeechHandler
import threading


class AudioVisualizer:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = screen.get_size()

        self.square_size = min(self.width, self.height) * 0.6
        self.left_bound = (self.width - self.square_size) / 2
        self.right_bound = (self.width + self.square_size) / 2
        self.top_bound = (self.height - self.square_size) / 2
        self.bottom_bound = (self.height + self.square_size) / 2

        self.stream = pyaudio.PyAudio().open(
            format=pyaudio.paInt16,
            channels=1,
            rate=44100,
            input=True,
            frames_per_buffer=4096
        )
        self.activate_visualization = False
        self.recognition_thread = None
        self.recognition_lock = threading.Lock()

        self.speech_handler = SpeechHandler()

        self.viz_surface = pygame.Surface((self.width, self.height), flags=pygame.SRCALPHA)
        self.bloom_surface = pygame.Surface((self.width, self.height), flags=pygame.SRCALPHA)

        self.prev_points = []

    def clamp_color(self, value):
        return max(0, min(255, value))
    
    def cosine_window(self, n, N):
        return (1 - np.cos(2 * np.pi * n / N)) / 2

    def gradient_color(self, value):
        r = int(255 * abs(value))
        g = 255 - r
        b = 255 - r

        r = self.clamp_color(r)
        g = self.clamp_color(g)
        b = self.clamp_color(b)
        return 0, 255, 255

    def draw_line(self, x1, y1, x2, y2, intensity):
        color = (0, 255, 255)
        width = int(3 * (intensity + 2) / 3)  # Modify this formula as needed to adjust the effect
        pygame.draw.line(self.viz_surface, color, (x1, y1), (x2, y2), width)

    def draw_bezier_curve(self, points, intensity):
        color = (71, 126, 189)
        width = int(3 * (intensity + 2) / 3)  # Modify this formula as needed to adjust the effect
        curve_points = self.bezier_curve(self.viz_surface, color, points, width)
        return curve_points[-1]
    
    def smooth_data(self, data, window_size=5):
        return [np.mean(data[max(0, i-window_size):i+window_size]) for i in range(len(data))]


    def bezier_curve(self, surface, color, points, width=1):
        
        # Cubic Bezier curve equation
        def calculate_bezier_point(t, p0, p1, p2, p3):
            x = (1 - t)**3 * p0[0] + 3 * (1 - t)**2 * t * p1[0] + 3 * (1 - t) * t**2 * p2[0] + t**3 * p3[0]
            y = (1 - t)**3 * p0[1] + 3 * (1 - t)**2 * t * p1[1] + 3 * (1 - t) * t**2 * p2[1] + t**3 * p3[1]
            return (x, y)

        # Generate the curve points
        curve_points = [calculate_bezier_point(t/100, points[0], points[1], points[2], points[3]) for t in range(101)]
        
        for i in range(1, len(curve_points)):
            pygame.draw.line(surface, color, curve_points[i-1], curve_points[i], width)

        return curve_points[-1]

    def apply_bloom(self):
        small = pygame.transform.smoothscale(self.viz_surface, (self.width//4, self.height//4))
        self.bloom_surface = pygame.transform.smoothscale(small, (self.width, self.height))
        
        self.bloom_surface.set_alpha(20)  # Adjust alpha as needed
        self.screen.blit(self.bloom_surface, (0, 0))
        self.viz_surface.set_alpha(255)
        self.screen.blit(self.viz_surface, (0, 0))
        self.viz_surface.fill((0, 0, 0, 0))

    def check_activation_word(self, raw_audio_data):
        with self.recognition_lock:
            if self.recognition_thread is None or not self.recognition_thread.is_alive():
                self.recognition_thread = threading.Thread(target=self.background_recognition, args=(raw_audio_data,))
                self.recognition_thread.start()

    def background_recognition(self, raw_audio_data):
        if self.speech_handler.check_activation_word(raw_audio_data):
            self.activate_visualization = True


    def update_visualization(self):
        raw_audio_data = self.stream.read(4096)
        self.check_activation_word(raw_audio_data)
        audio_data = np.frombuffer(raw_audio_data, dtype=np.int16)
        audio_data = audio_data / np.max(np.abs(audio_data), axis=0)

        
        if self.activate_visualization:
            avg_audio_data = [np.mean(audio_data[i:i+10]) for i in range(0, len(audio_data), 100)]
            smoothed_data = self.smooth_data(avg_audio_data, window_size=8)

            step = self.square_size / len(smoothed_data)

            for i in range(2, len(smoothed_data) - 2):
                window_val = self.cosine_window(i, len(smoothed_data))
                
                x0 = self.left_bound + step * (i - 2)
                y0 = (self.height / 2) + smoothed_data[i - 2] * (self.square_size / 4) * window_val

                x1 = self.left_bound + step * (i - 1)
                y1 = (self.height / 2) + smoothed_data[i - 1] * (self.square_size / 4) * window_val

                x2 = self.left_bound + step * i
                y2 = (self.height / 2) + smoothed_data[i] * (self.square_size / 4) * window_val

                x3 = self.left_bound + step * (i + 1)
                y3 = (self.height / 2) + smoothed_data[i + 1] * (self.square_size / 4) * window_val

                bezier_points = [(x0, y0), (x1, y1), (x2, y2), (x3, y3)]
                intesity = abs(smoothed_data[i])
                last_y = self.draw_bezier_curve(bezier_points, intesity)

            self.apply_bloom()

        else:
            a = pygame.draw.line(self.screen, (71, 126, 189, 10), (self.left_bound, self.height / 2), (self.right_bound, self.height / 2), 3)

        

