# 🎙️ Emotion Voice Assistant

An AI-powered voice assistant that combines **speech-to-text, voice emotion analysis, emotion-aware response policies, an LLM response layer, and text-to-speech** in a Flask web application.

## ✨ Features

- 🎤 Upload short voice recordings from a browser
- 📝 Speech-to-text with Faster-Whisper
- 🧠 Voice emotion classification using pitch, energy, and tempo signals
- 🤝 Emotion-aware response strategies
- 💬 Optional local Ollama LLM integration with safe fallback responses
- 🔊 Text-to-speech response generation
- 🌐 Flask web interface
- ❤️ Health-check endpoint for deployment monitoring
- 🔒 Temporary audio processing instead of storing user input permanently

## 🏗️ Architecture

```text
Voice Upload
     ↓
Temporary Audio File
     ↓
 ┌───────────────┐
 │ Audio Analysis│ → Emotion
 └───────────────┘
     ↓
 Faster-Whisper → Transcript
     ↓
 Emotion + Transcript + Policy
     ↓
 Ollama LLM (optional)
     ↓
 Fallback response if LLM unavailable
     ↓
 Text-to-Speech
     ↓
 Browser Audio Player
```

## 🛠️ Tech Stack

- **Python / Flask** — backend and API
- **Librosa / NumPy** — audio feature extraction and emotion heuristics
- **Faster-Whisper** — speech recognition
- **Ollama** — optional local LLM response generation
- **pyttsx3** — text-to-speech
- **HTML / CSS / JavaScript** — browser UI
- **Gunicorn** — production WSGI server

## 🚀 Local Setup

### 1. Clone

```bash
git clone https://github.com/SIDMINUL/Emotion-Voice-Assistant.git
cd Emotion-Voice-Assistant
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Optional: enable Ollama

Install Ollama separately and make sure the configured model is available. By default EVA uses:

```text
http://localhost:11434/api/generate
llama3
```

You can override these with environment variables:

```bash
OLLAMA_URL=http://localhost:11434/api/generate
OLLAMA_MODEL=llama3
```

EVA still returns a built-in empathetic response when Ollama is unavailable.

### 4. Run

From the repository root:

```bash
python EVA/app.py
```

Then open `http://localhost:5000`.

For production-style local testing:

```bash
gunicorn --chdir EVA app:app --bind 0.0.0.0:5000
```

## ☁️ Deployment

The repository includes `render.yaml` for Render deployment.

> **Important:** The current application uses local Ollama and `pyttsx3`. These components are environment-dependent and may not work on every cloud runtime. The API remains usable without Ollama because of the built-in response fallback, but cloud TTS support should be verified on the target platform.

## 🔌 API

### `GET /health`

Returns:

```json
{"status":"ok","service":"emotion-voice-assistant"}
```

### `POST /process`

Accepts a multipart form upload with the field name `audio` and returns the transcript, detected emotion, response strategy, generated response, and audio URL.

## 📁 Project Structure

```text
Emotion-Voice-Assistant/
├── EVA/
│   ├── app.py
│   ├── audio/
│   │   ├── features.py
│   │   ├── recorder.py
│   │   └── speech_to_text.py
│   ├── llm/
│   │   └── response_generator.py
│   ├── models/
│   │   ├── emotion_model.py
│   │   └── policy_model.py
│   ├── templates/
│   │   └── index.html
│   └── tts/
│       └── speech.py
├── requirements.txt
├── render.yaml
└── README.md
```

## ⚠️ Limitations

The emotion detector is a lightweight heuristic system based on acoustic features; it is **not a clinically validated emotion-recognition model**. Results can vary with microphone quality, speaker characteristics, background noise, and language.

## 👨‍💻 Author

**Abdul Momin Siddiqui**  
GitHub: **SIDMINUL**
