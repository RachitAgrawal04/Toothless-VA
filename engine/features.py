from playsound import playsound
import threading
import eel
import os

# Absolute path to the startup sound, relative to this file's location
_BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_SOUND_PATH = os.path.join(_BASE_DIR, 'www', 'assets', 'audio', 'start_sound.mp3')

# Function to play assistant sound

@eel.expose
def play_assistant_sound():
    # Run sound playback in a separate thread to avoid blocking the UI
    threading.Thread(target=playsound, args=(_SOUND_PATH,), daemon=True).start()