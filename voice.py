import pyttsx3


def speak(text):
    if not text:
        return

    engine = pyttsx3.init()

    voices = engine.getProperty("voices")

    # Microsoft Zira — feminine English voice
    for voice in voices:
        if "Zira" in voice.name:
            engine.setProperty("voice", voice.id)
            break

    engine.setProperty("rate", 175)
    engine.setProperty("volume", 1.0)

    engine.say(str(text))
    engine.runAndWait()

    engine.stop()