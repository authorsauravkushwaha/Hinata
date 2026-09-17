import json
import queue

import sounddevice as sd
from vosk import Model, KaldiRecognizer


MODEL_PATH = "models/vosk-model-small-en-us-0.15"
SAMPLE_RATE = 16000
MICROPHONE_DEVICE = 1

audio_queue = queue.Queue()


def audio_callback(indata, frames, time, status):
    if status:
        print("Audio status:", status)

    audio_queue.put(bytes(indata))


def listen():
    print("Loading Vosk...")
    model = Model(MODEL_PATH)
    recognizer = KaldiRecognizer(model, SAMPLE_RATE)

    print("Listening...")
    print("Say: Hello Hinata")

    with sd.RawInputStream(
        samplerate=SAMPLE_RATE,
        blocksize=4000,
        device=MICROPHONE_DEVICE,
        dtype="int16",
        channels=1,
        callback=audio_callback
    ):
        while True:
            data = audio_queue.get()

            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                text = result.get("text", "").strip()

                if text:
                    return text


if __name__ == "__main__":
    recognized_text = listen()
    print("You said:", recognized_text)