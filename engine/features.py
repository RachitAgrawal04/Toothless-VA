from playsound import playsound
import eel

# Function to play assistant sound

@eel.expose
def play_assistant_sound():
    music_dir = 'www/assets/audio/start_sound.mp3'
    playsound(music_dir)