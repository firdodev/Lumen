import pygame
import pyaudio
import numpy as np
import speech_recognition as sr
from Lumen.Core.SpeechHandler import SpeechHandler


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
        
        self.speech_handler = SpeechHandler()

    def draw_bloom(self, x1, y1, x2, y2):
        aqua = (0, 255, 255)
        for offset in range(2, 8):
            pygame.draw.line(self.screen, aqua, (x1, y1), (x2, y2), offset)

    def check_activation_word(self, raw_audio_data):
        audio_data = sr.AudioData(raw_audio_data, sample_rate=44100, sample_width=2)
        try:
            detected_text = self.recognizer.recognize_google(audio_data)
            print(detected_text)
            if "Lumen" in detected_text:
                self.activate_visualization = True
        except sr.UnknownValueError:
            print("Audio not understood or too noisy.")
        except Exception as e:
            print("Error:", e)


    def update_visualization(self):
        raw_audio_data = self.stream.read(4096)
        audio_data = np.frombuffer(raw_audio_data, dtype=np.int16)
        audio_data = audio_data / np.max(np.abs(audio_data), axis=0)

        self.screen.fill((0, 0, 0))
        
        # Visualize only if "Lumen" was detected
        if self.speech_handler.check_activation_word(raw_audio_data):
            avg_audio_data = [np.mean(audio_data[i:i+4]) for i in range(0, len(audio_data), 4)]
            self.activate_visualization = True
            step = self.square_size / len(avg_audio_data)
            for i in range(1, len(avg_audio_data)):
                x1 = self.left_bound + step * (i - 1)
                y1 = (self.height / 2) + avg_audio_data[i - 1] * (self.square_size / 2)
                x2 = self.left_bound + step * i
                y2 = (self.height / 2) + avg_audio_data[i] * (self.square_size / 2)
                self.draw_bloom(x1, y1, x2, y2)
            
        else:
            # Draw a straight line if not activated
            pygame.draw.line(self.screen, (0, 255, 255), (self.left_bound, self.height / 2), (self.right_bound, self.height / 2), 3)
        

