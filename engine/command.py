import pyttsx3
import speech_recognition as sr
from speech_recognition import WaitTimeoutError
import eel
import webbrowser
import datetime
import wikipedia
import os
import sys
import random

def speak(text):
    try:
        if sys.platform == 'win32':
            engine = pyttsx3.init('sapi5')
            voices = engine.getProperty('voices')
            # Use female voice if available
            if len(voices) > 1:
                engine.setProperty('voice', voices[1].id)
        else:
            engine = pyttsx3.init()
        engine.setProperty('rate', 178)
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"TTS error: {e}")


def allCommands(query):
    """Route a recognized query to the appropriate handler and return a response."""
    query = query.lower().strip()

    # Greetings
    if any(w in query for w in ['hello', 'hi', 'hey', 'greetings']):
        response = "Hello! I'm Toothless, your personal voice assistant. How can I help you?"
        speak(response)
        return response

    # Identity
    if any(w in query for w in ['who are you', 'what are you', 'your name', 'introduce yourself']):
        response = "I'm Toothless, a dragon-themed personal voice assistant. I can tell you the time, date, search Wikipedia, open websites, and more!"
        speak(response)
        return response

    # Time
    if any(w in query for w in ['time', 'what time']):
        now = datetime.datetime.now().strftime("%I:%M %p")
        response = f"The current time is {now}."
        speak(response)
        return response

    # Date
    if any(w in query for w in ['date', 'today', "what's today", 'what day']):
        today = datetime.datetime.now().strftime("%A, %B %d, %Y")
        response = f"Today is {today}."
        speak(response)
        return response

    # Open YouTube
    if 'youtube' in query:
        search_query = query.replace('open youtube', '').replace('search youtube for', '').replace('youtube', '').strip()
        if search_query:
            url = f"https://www.youtube.com/results?search_query={search_query.replace(' ', '+')}"
        else:
            url = "https://www.youtube.com"
        webbrowser.open(url)
        response = f"Opening YouTube{' for ' + search_query if search_query else ''}."
        speak(response)
        return response

    # Open Google
    if 'google' in query:
        search_query = query.replace('open google', '').replace('search google for', '').replace('google', '').strip()
        if search_query:
            url = f"https://www.google.com/search?q={search_query.replace(' ', '+')}"
        else:
            url = "https://www.google.com"
        webbrowser.open(url)
        response = f"Searching Google{' for ' + search_query if search_query else ''}."
        speak(response)
        return response

    # Wikipedia search
    if 'wikipedia' in query or query.startswith('what is') or query.startswith('who is') or query.startswith('tell me about'):
        search_term = (query.replace('wikipedia', '')
                           .replace('what is', '')
                           .replace('who is', '')
                           .replace('tell me about', '')
                           .strip())
        if search_term:
            try:
                eel.displayMessage(f"Searching Wikipedia for {search_term}...")
                result = wikipedia.summary(search_term, sentences=2)
                speak(result)
                return result
            except wikipedia.exceptions.DisambiguationError as e:
                response = f"That topic is ambiguous. Did you mean: {', '.join(e.options[:3])}?"
                speak(response)
                return response
            except wikipedia.exceptions.PageError:
                response = f"Sorry, I couldn't find anything on Wikipedia about {search_term}."
                speak(response)
                return response
            except Exception as e:
                print(f"Wikipedia error: {e}")
                response = "Sorry, I had trouble searching Wikipedia."
                speak(response)
                return response

    # Goodbye
    if any(w in query for w in ['bye', 'goodbye', 'see you', 'exit', 'quit']):
        response = "Goodbye! It was a pleasure assisting you. Toothless out!"
        speak(response)
        return response

    # Jokes
    if any(w in query for w in ['joke', 'funny', 'laugh', 'make me laugh']):
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? Because he was outstanding in his field.",
            "I told my computer I needed a break. Now it won't stop sending me Kit-Kat ads.",
            "Why do programmers prefer dark mode? Because light attracts bugs.",
            "What do you call a fish without eyes? A fsh.",
            "I'm reading a book about anti-gravity. It's impossible to put down.",
        ]
        response = random.choice(jokes)
        speak(response)
        return response

    # Help
    if any(w in query for w in ['help', 'what can you do', 'commands', 'features']):
        response = ("I can help you with: current time and date, opening YouTube or Google, "
                    "searching Wikipedia, telling jokes, and more. Just ask!")
        speak(response)
        return response

    # Default: echo back
    response = f"You said: {query}. I'm still learning new tricks. Try asking me the time, date, or to open a website!"
    speak(response)
    return response


@eel.expose
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        eel.displayMessage("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source, 10, 7)
        except WaitTimeoutError:
            print("Listening timed out. No phrase detected.")
            eel.displayMessage("Listening timed out. No phrase detected.")
            return "None"

    try:
        print("Recognizing...")
        eel.displayMessage("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        eel.displayMessage(f"User said: {query}")
        return allCommands(query)

    except Exception as e:
        print("Say that again please...")
        eel.displayMessage("Say that again please...")
        return "None"


@eel.expose
def processText(text):
    """Process a typed text command from the UI."""
    if not text or not text.strip():
        return "Please type something first."
    eel.displayMessage(f"You typed: {text}")
    return allCommands(text)

