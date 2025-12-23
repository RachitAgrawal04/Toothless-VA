import pyttsx3
import speech_recognition as sr
from speech_recognition import WaitTimeoutError
import eel

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 178)
    engine.say(text)
    engine.runAndWait()

#speak("This was supposed to be Hiccup's voice, but i suppose this will do for now.")

@eel.expose
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        eel.DisplayMessage("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source, 10, 7)
        except WaitTimeoutError:
            print("Listening timed out. No phrase detected.")
            eel.DisplayMessage("Listening timed out. No phrase detected.")
            return "None"

    try:
        print("Recognizing...")
        eel.DisplayMessage("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        eel.DisplayMessage(f"User said: {query}\n")
        speak(query)
        return query.lower()

    except Exception as e:
        print("Say that again please...")
        eel.DisplayMessage("Say that again please...")
        return "None"

