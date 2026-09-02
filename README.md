# 🎙️ Emotion Voice Assistant (EVA)

> An emotion-aware voice assistant that listens to a user's voice, analyzes acoustic signals, understands speech, and generates a context-aware response.

**Live Demo:** https://emotion-voice-assistant.onrender.com

## ✨ Overview

Emotion Voice Assistant (EVA) is a Flask-based AI application that combines **speech recognition, voice emotion analysis, response policies, and conversational response generation** into a simple web interface.

The system is designed as an end-to-end AI pipeline rather than a single prediction model:

**Voice → Emotion → Speech-to-Text → Response Strategy → AI Response → Voice Output**

EVA can detect broad emotional states from acoustic characteristics such as energy, pitch, and speaking rate, then adapt its response style accordingly.

## 🚀 Features

- 🎤 Upload short **WAV voice recordings** through a browser
- 📝 Speech-to-text using a lightweight speech-recognition pipeline
- 🧠 Acoustic emotion detection using pitch, energy, and speaking rate
- 🤝 Emotion-aware response policies
- 💬 Optional Ollama integration for locally generated responses
- 🛡️ Built-in fallback responses when the LLM is unavailable
- 🔊 Browser-based text-to-speech using Web Speech API
- 🌐 Responsive Flask web interface
- ❤️ `/health` endpoint for deployment monitoring
- 🔒 Uploaded audio is processed temporarily and removed after processing
- ☁️ Production deployment configuration for Render

## 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │   Browser / User    │
                    │   Upload WAV Audio  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Flask `/process`  │
                    └──────────┬──────────┘
                               │
                ┌──────────────┴──────────────┐
                ▼                             ▼
       ┌─────────────────┐           ┌─────────────────┐
       │ Emotion Engine  │           │ Speech-to-Text  │
       │ Pitch / Energy  │           │ Audio → Text    │
       │ Speaking Rate   │           └────────┬────────┘
       └────────┬────────┘                    │
                └──────────────┬─────────────┘
                               ▼
                    ┌─────────────────────┐
                    │ Response Policy     │
                    │ Emotion-aware style │
                    └──────────┬──────────┘
                               ▼
                    ┌─────────────────────┐
                    │ Response Generator  │
                    │ Ollama / Fallback   │
                    └──────────┬──────────┘
                               ▼
                    ┌─────────────────────┐
                    │ Browser Speech      │
                    │ Web Speech API      │
                    └─────────────────────┘
```

## 🧠 How It Works

### 1. Voice Input
The user uploads a short WAV recording through the web interface.

### 2. Emotion Detection
EVA extracts lightweight acoustic signals:

- **Energy** — estimates vocal intensity
- **Pitch** — estimates the dominant fundamental-frequency range
- **Speaking rate** — estimates speech activity events per minute

A rule-based classifier maps these signals to broad states such as **sad, angry, excited, or neutral**.

### 3. Speech Recognition
The uploaded recording is converted into text so EVA can understand the user's message.

### 4. Response Policy
The detected emotion is mapped to a response strategy. For example, a sad input can trigger a more empathetic response style, while an angry input can receive a supportive and de-escalating style.

### 5. Response Generation
If Ollama is configured, EVA can use a local LLM to generate a response using the transcript, emotion, and selected response strategy. If Ollama is unavailable, EVA uses a safe built-in fallback response.

### 6. Voice Output
The response is spoken directly in the browser using the Web Speech API, avoiding server-side TTS dependencies.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Flask | Web server and REST API |
| NumPy | Numerical/audio signal processing |
| SoundFile | WAV audio loading |
| Speech Recognition | Speech-to-text |
| Ollama | Optional local LLM response generation |
| HTML/CSS/JavaScript | Frontend interface |
| Web Speech API | Browser text-to-speech |
| Gunicorn | Production WSGI server |
| Render | Cloud deployment |

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

## 🚀 Run Locally

### Clone the repository

```bash
git clone https://github.com/SIDMINUL/Emotion-Voice-Assistant.git
cd Emotion-Voice-Assistant
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Start the Flask application

```bash
python EVA/app.py
```

Open:

```text
http://localhost:5000
```

### Production-style local run

```bash
gunicorn --chdir EVA app:app --bind 0.0.0.0:5000
```

## 🤖 Optional Ollama Integration

EVA can use Ollama for locally generated responses.

Set:

```bash
OLLAMA_URL=http://localhost:11434/api/generate
OLLAMA_MODEL=llama3
```

If Ollama is not available, EVA automatically falls back to predefined emotion-aware responses.

## ☁️ Deployment

The project includes a `render.yaml` configuration for deployment on Render.

The deployed application is available here:

**https://emotion-voice-assistant.onrender.com**

The cloud version uses a lightweight processing path and browser speech output so that the application can run within constrained cloud resources.

## 🔌 API

### `GET /health`

Health check:

```json
{
  "status": "ok",
  "service": "emotion-voice-assistant"
}
```

### `POST /process`

Accepts a multipart form upload:

```text
audio=<WAV file>
```

Example response:

```json
{
  "text": "Hello, how are you?",
  "emotion": "neutral",
  "action": "neutral",
  "response": "I'm listening. How can I help?",
  "audio": null
}
```

## ⚠️ Limitations

- Emotion detection is a **lightweight heuristic system**, not a clinically validated emotion-recognition model.
- Acoustic emotion classification can be affected by microphone quality, background noise, speaker characteristics, language, and recording conditions.
- Voice output uses the browser's Web Speech API, so available voices depend on the user's browser and operating system.
- Ollama is optional and primarily intended for local/self-hosted use.
- Short, clear WAV recordings provide the most reliable results.

## 🔐 Privacy

Uploaded audio is stored temporarily during processing and removed after the request completes. The application does not intentionally persist the uploaded voice recording.

## 👨‍💻 Author

**Abdul Momin Siddiqui**

GitHub: **SIDMINUL**

---

⭐ If you find this project useful, consider giving the repository a star.