import subprocess
import pkg_resources

# List of required packages
REQUIRED_PACKAGES = ["pyaudio", "numpy", "pygame", "SpeechRecognition", "openai", "pyttsx3"]

installed_packages = {pkg.key for pkg in pkg_resources.working_set}

for package in REQUIRED_PACKAGES:
    if package not in installed_packages:
        subprocess.check_call(["pip", "install", package])
