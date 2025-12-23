import pyttsx3
import speech_recognition as sr
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
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 10, 7)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        speak(query)

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query.lower()

