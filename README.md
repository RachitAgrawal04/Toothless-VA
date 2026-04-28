# 🐉 Toothless — AI Voice Assistant

<p align="center">
  <img src="www/assets/img/toothless_icon.jpg" alt="Toothless VA Icon" width="120"/>
</p>

<p align="center">
  A sleek, dragon-themed desktop virtual assistant powered by Python and a modern web UI — inspired by the Night Fury from <em>How to Train Your Dragon</em>.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python" />
  <img src="https://img.shields.io/badge/Eel-0.16.0-green" />
  <img src="https://img.shields.io/badge/Speech%20Recognition-Google-red?logo=google" />
  <img src="https://img.shields.io/badge/TTS-pyttsx3%20%7C%20SAPI5-purple" />
  <img src="https://img.shields.io/badge/Platform-Windows-lightgrey?logo=windows" />
</p>

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Assistant](#running-the-assistant)
- [How It Works](#-how-it-works)
- [Roadmap & Future Goals](#-roadmap--future-goals)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🌟 Overview

**Toothless** is a desktop AI voice assistant that combines a Python backend with a visually rich web-based front end. When launched, it greets you with a startup sound, opens a full-screen app in Microsoft Edge, and waits for your voice or text commands — all wrapped in a dark, animated UI reminiscent of Toothless the Night Fury dragon.

The assistant bridges Python logic and browser UI using the [Eel](https://github.com/python-eel/Eel) library, giving it the responsiveness of a web app with the full power of Python's ecosystem for AI and automation.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🎤 **Voice Input** | Captures microphone input using the Google Speech Recognition API |
| 🔊 **Text-to-Speech** | Speaks responses back using `pyttsx3` (SAPI5, female voice) |
| 🌊 **Siri-style Wave UI** | Animated iOS 9–style waveform (via SiriWave.js) during listening |
| 💬 **Real-time Messages** | Status and recognized text displayed live in the UI via Eel's Python↔JS bridge |
| 🎵 **Startup Sound** | Plays a startup audio cue on launch (non-blocking background thread) |
| ⌨️ **Text Chat Input** | Text input box for typing commands (foundation for chat mode) |
| ⚙️ **Settings Button** | Placeholder for future configuration options |
| 🎨 **Animated Orb UI** | A pulsing, rotating orb on the home screen with CSS animations |
| 🖥️ **Desktop App Feel** | Runs in Edge's `--app` mode (no browser chrome / address bar) |

---

## 🛠 Tech Stack

### Backend (Python)
| Library | Purpose |
|---|---|
| [`eel`](https://github.com/python-eel/Eel) | Python ↔ JavaScript bridge, local web server |
| [`pyttsx3`](https://github.com/nateshmbhat/pyttsx3) | Offline text-to-speech (Windows SAPI5) |
| [`SpeechRecognition`](https://github.com/Uberi/speech_recognition) | Microphone capture + Google Speech-to-Text |
| [`playsound`](https://github.com/TaylorSMarks/playsound) | Play the startup MP3 sound effect |
| `threading` | Non-blocking sound and future async operations |

### Frontend (Web)
| Technology | Purpose |
|---|---|
| HTML5 / CSS3 / JavaScript | Core UI structure and styling |
| [Bootstrap 5](https://getbootstrap.com/) | Responsive layout and icon library |
| [jQuery 3](https://jquery.com/) | DOM manipulation and event handling |
| [SiriWave.js](https://github.com/kopiro/siriwave) | iOS 9-style listening waveform animation |
| [Textillate.js](https://textillate.js.org/) | Animated text effects for messages |
| [Modernizr](https://modernizr.com/) | Feature detection for particles |

---

## 📁 Project Structure

```
Toothless-VA/
├── main.py                  # Entry point — initializes Eel and launches the app
├── engine/
│   ├── command.py           # Voice capture (microphone → Google STT) & TTS
│   └── features.py          # Startup sound and Eel-exposed Python features
├── www/                     # Front-end web assets (served by Eel)
│   ├── index.html           # Main UI page
│   ├── style.css            # Dark theme, animations, input styling
│   ├── main.js              # Siri wave, text animations, mic/back button logic
│   ├── controller.js        # Eel message display handler (Python → UI)
│   ├── script.js            # Particle.js canvas setup
│   └── assets/
│       ├── audio/
│       │   └── start_sound.mp3   # Startup sound effect
│       ├── img/
│       │   └── toothless_icon.jpg
│       └── vendore/
│           └── texllate/         # Textillate.js + animate.css + helpers
└── envtoothless/            # Python virtual environment (git-ignored)
```

---

## 🚀 Getting Started

### Prerequisites

- **Windows 10/11** (required for SAPI5 TTS and `msedge.exe` launcher)
- **Python 3.10+**
- **Microsoft Edge** browser
- A working **microphone**

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/RachitAgrawal04/Toothless-VA.git
   cd Toothless-VA
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv envtoothless
   envtoothless\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install eel pyttsx3 SpeechRecognition playsound
   ```
   > **Note:** `SpeechRecognition` requires PyAudio for microphone access. Install it via:
   > ```bash
   > pip install pyaudio
   > ```
   > If PyAudio fails to install, download the matching wheel from [Christoph Gohlke's site](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install with `pip install <wheel_file>.whl`.

### Running the Assistant

```bash
python main.py
```

Toothless will:
1. Play the startup sound
2. Open the assistant UI in Microsoft Edge (app mode)
3. Wait for you to click the 🎤 mic button and speak

---

## ⚙️ How It Works

```
User clicks Mic
      │
      ▼
main.js calls eel.takecommand()
      │
      ▼
command.py captures audio via microphone
      │
      ▼
Google Speech Recognition converts audio → text
      │
      ├──► eel.displayMessage() updates the SiriWave UI in real-time
      │
      ▼
pyttsx3 speaks the recognized text aloud
      │
      ▼
Query returned to main.js for further processing
```

The **Eel** library keeps a WebSocket connection between Python and the browser, allowing functions decorated with `@eel.expose` to be called directly from JavaScript and vice versa.

---

## 🗺 Roadmap & Future Goals

Toothless is designed to grow into a fully capable personal assistant. Here's what's planned:

### 🔧 Core Improvements
- [ ] **Natural Language Processing (NLP)** — Integrate spaCy or a local LLM (e.g., Ollama) to understand intent, not just transcribe speech
- [ ] **Command Router** — Parse recognized queries and route them to specific skill handlers (open app, search web, set timer, etc.)
- [ ] **Text Chat Mode** — Fully wire up the text input box to process typed commands through the same pipeline as voice

### 🌐 Skills & Integrations
- [ ] **Web Search** — Search Google/DuckDuckGo and read back top results
- [ ] **Wikipedia Summaries** — Answer factual questions via the Wikipedia API
- [ ] **Weather & News** — Fetch real-time weather and news headlines
- [ ] **Application Launcher** — Open apps, files, and URLs by voice command
- [ ] **System Controls** — Control volume, brightness, clipboard, and screen lock
- [ ] **Calendar & Reminders** — Create and read events from Google Calendar
- [ ] **Music Player Control** — Pause/play/skip Spotify or local media

### 🎨 UI / UX
- [ ] **Settings Panel** — Wire up the ⚙️ settings button: choose voice gender, language, startup behavior
- [ ] **Command History** — Display a scrollable log of past interactions
- [ ] **Custom Wake Word** — Trigger Toothless hands-free ("Hey Toothless!")
- [ ] **Toothless Avatar Animation** — Add an animated dragon avatar that reacts to speech

### 🖥️ Platform & Packaging
- [ ] **Cross-platform support** — Replace Windows-specific SAPI5 and `msedge.exe` with platform-agnostic alternatives (e.g., `espeak`, system browser detection)
- [ ] **Installer / Executable** — Package as a standalone `.exe` with PyInstaller
- [ ] **Auto-start on Login** — Optional system tray mode that starts Toothless with Windows

---

## 🤝 Contributing

Contributions, ideas, and bug reports are welcome! To contribute:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m "Add my feature"`
4. Push to your fork: `git push origin feature/my-feature`
5. Open a Pull Request

Please keep code style consistent with the existing project and test voice functionality before submitting.

---

## 📄 License

This project is open source. License file to be added. For now, feel free to use, modify, and share with attribution.

---

<p align="center">
  Made with 🖤 and a love for dragons &nbsp;·&nbsp; <em>"A dragon and his boy."</em>
</p>
