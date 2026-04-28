import os
import sys
import eel
from engine.features import *
from engine.command import *

eel.init('www')

play_assistant_sound()

# Cross-platform browser launch — Eel's built-in modes handle this,
# but as a fallback we also open the URL via webbrowser.
import webbrowser
import threading

def _open_browser():
    import time
    time.sleep(1)  # Give Eel's server a moment to start
    webbrowser.open('http://localhost:8000/index.html')

if sys.platform == 'win32':
    os.system('start msedge.exe --app=http://localhost:8000/index.html')
else:
    threading.Thread(target=_open_browser, daemon=True).start()

eel.start('index.html', mode=None, host='localhost', block=True)
