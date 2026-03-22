"""
Speech-to-text using Whisper
"""
import whisper

# Load model once (VERY important for performance)
model = whisper.load_model("base")

def transcribe(audio_path):
    """
    Converts speech audio into text using Whisper.

    Parameters:
    - audio_path (str): Path to WAV file

    Returns:
    - text (str): Transcribed text
    """

    print("🧠 Transcribing...")

    result = model.transcribe(audio_path)

    text = result["text"].strip()

    print(f"📝 You said: {text}")

    return text
import whisper

# Load model once (VERY important for performance)
model = whisper.load_model("base")

def transcribe(audio_path):
    """
    Converts speech audio into text using Whisper.

    Parameters:
    - audio_path (str): Path to WAV file

    Returns:
    - text (str): Transcribed text
    """

    print("🧠 Transcribing...")

    result = model.transcribe(audio_path)

    text = result["text"].strip()

    print(f"📝 You said: {text}")

    return text