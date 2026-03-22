"""
Microphone input handler
"""
import sounddevice as sd
from scipy.io.wavfile import write
import uuid

def record_audio(duration=5, sample_rate=44100):
    """
    Records audio from the microphone and saves it to a WAV file.

    Parameters:
    - duration (int): Recording time in seconds
    - sample_rate (int): Audio sampling frequency

    Returns:
    - file_path (str): Path to saved audio file
    """

    print("🎤 Recording...")

    # Generate a unique filename to avoid overwriting
    file_path = f"temp_{uuid.uuid4().hex}.wav"

    # Record audio
    audio = sd.rec(
        int(duration * sample_rate),  # total frames
        samplerate=sample_rate,
        channels=1,
        dtype='int16'
    )

    sd.wait()  # Block until recording is finished

    write(file_path, sample_rate, audio)

    print("✅ Recording complete")

    return file_path
import sounddevice as sd
from scipy.io.wavfile import write
import uuid

def record_audio(duration=5, sample_rate=44100):
    """
    Records audio from the microphone and saves it to a WAV file.

    Parameters:
    - duration (int): Recording time in seconds
    - sample_rate (int): Audio sampling frequency

    Returns:
    - file_path (str): Path to saved audio file
    """

    print("🎤 Recording...")

    # Generate a unique filename to avoid overwriting
    file_path = f"temp_{uuid.uuid4().hex}.wav"

    # Record audio
    audio = sd.rec(
        int(duration * sample_rate),  # total frames
        samplerate=sample_rate,
        channels=1,
        dtype='int16'
    )

    sd.wait()  # Block until recording is finished

    write(file_path, sample_rate, audio)

    print("✅ Recording complete")

    return file_path