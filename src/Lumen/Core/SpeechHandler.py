import speech_recognition as sr
import json
import os

class SpeechHandler:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 3000

        current_directory = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(current_directory, '..', 'config.json')
        
        with open(config_path, 'r') as file:
            config = json.load(file)
            self.activation_word = config.get('name', '').lower()  # Use a default empty string if not found

    def check_activation_word(self, raw_audio_data):
        print("Listening...")
        try:
            with sr.Microphone() as source2:
                self.recognizer.adjust_for_ambient_noise(source2, duration=0.2)
                audio = self.recognizer.listen(source2, timeout=5, phrase_time_limit=5)

                detected_text = self.recognizer.recognize_google(audio)
                print(detected_text)
                if self.activation_word in detected_text.lower():
                    return True
                return False
        except sr.UnknownValueError:
            print("Audio not understood or too noisy.")
            return False
        except Exception as e:
            print("Error:", e)
            return False
