"""
Text-to-speech output
"""
import pyttsx3

# Initialize engine once
engine = pyttsx3.init()

def speak(text):
    """
    Converts text into speech output.
    """

    print(f"🔊 Speaking: {text}")

    engine.say(text)
    engine.runAndWait()
import pyttsx3

# Initialize engine once
engine = pyttsx3.init()

def speak(text):
    """
    Converts text into speech output.
    """

    print(f"🔊 Speaking: {text}")

    engine.say(text)
    engine.runAndWait()