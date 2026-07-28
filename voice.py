import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone(device_index=1) as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
    try:
        text = recognizer.recognize_google(audio)
        return text

    except sr.UnknownValueError:
        return None

    except sr.RequestError:
        return None


if __name__ == "__main__":
    result = listen()

    if result:
        print("You said:", result)
    else:
        print("Sorry, I couldn't understand.")