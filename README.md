# 🎙️ Emotion Voice Assistant

An AI-powered web application that detects emotions from voice input and responds intelligently using NLP models. This project combines speech processing, emotion detection, and conversational AI to create an interactive assistant.

---

## 🚀 Features

- 🎤 Voice recording via browser
- 🧠 Emotion detection from speech
- 💬 AI-generated responses based on emotion
- 🌐 Full-stack web application (Frontend + Backend)
- ⚡ Real-time interaction
- 🎨 Modern UI with chatbox interface

---

## 🛠️ Tech Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python (Flask)
- Speech Processing Libraries
- OpenAI API (for intelligent responses)

---

## 📂 Project Structure

```
Emotion-Voice-Assistant/
│
├── static/
│   ├── script.js
│   ├── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/emotion-voice-assistant.git
cd emotion-voice-assistant
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Add API Key

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

---

### 5. Run the Application

```bash
python app.py
```

---

### 6. Open in Browser

```
http://127.0.0.1:5000/
```

---

## 🎯 How It Works

1. User clicks the mic button
2. Voice is recorded in browser
3. Audio sent to Flask backend
4. Emotion is detected from speech
5. AI generates response based on emotion
6. Response displayed in chat UI

---

## 🔥 Future Improvements

- Add real-time speech-to-text
- Improve emotion classification accuracy
- Add multi-language support
- Deploy on cloud (AWS / Render)

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo  
2. Create a new branch  
3. Make your changes  
4. Submit a pull request  

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Your Name  
GitHub: https://github.com/your-username
