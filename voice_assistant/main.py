"""
Orchestrator - Controls the flow of the voice assistant
"""
from audio.recorder import record_audio
from stt.whisper_stt import transcribe
from ai.brain import generate_response
from tts.speaker import speak

def run_assistant():
    """
    Main loop controlling the voice assistant pipeline.
    """

    print("🚀 Voice Assistant Started")

    while True:
        # Step 1: Capture audio
        audio_file = record_audio()

        # Step 2: Convert speech to text
        text = transcribe(audio_file)

        # Safety check (avoid empty input)
        if not text:
            print("⚠️ No speech detected")
            continue

        # Step 3: Generate response
        response = generate_response(text)

        # Step 4: Speak response
        speak(response)


if __name__ == "__main__":
    run_assistant()
