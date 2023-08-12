import speech_recognition as sr

class SpeechHandler:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def check_activation_word(self, raw_audio_data):
        try:
            with sr.Microphone() as source2:
                self.recognizer.adjust_for_ambient_noise(source2, duration=0.2)
                audio = self.recognizer.listen(source2)

                detected_text = self.recognizer.recognize_google(audio)
                print(detected_text)
                if "Lumen" in detected_text:
                    return True
                return False
        except sr.UnknownValueError:
            print("Audio not understood or too noisy.")
            return False
        except Exception as e:
            print("Error:", e)
            return False
