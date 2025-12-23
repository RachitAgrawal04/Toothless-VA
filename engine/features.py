from playsound import playsound
import threading
import eel

# Function to play assistant sound

@eel.expose
def play_assistant_sound():
    music_dir = 'www/assets/audio/start_sound.mp3'
    # Run sound playback in a separate thread to avoid blocking the UI
    threading.Thread(target=playsound, args=(music_dir,), daemon=True).start()