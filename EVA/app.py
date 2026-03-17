from flask import Flask, render_template, request, jsonify
import os

from audio.features import extract_features
from audio.speech_to_text import transcribe
from models.emotion_model import detect_emotion
from models.policy_model import choose_action
from llm.response_generator import generate_response
from tts.speech import text_to_speech

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process_audio():

    file = request.files["audio"]
    path = "input.wav"
    file.save(path)

    features = extract_features(path)

    emotion = detect_emotion(path)

    action = choose_action(emotion)

    text = transcribe(path)

    print("User said:", text)
    response = generate_response(text, emotion, action)

    audio_path = text_to_speech(response)

    return jsonify({
        "audio": audio_path
    })


if __name__ == "__main__":
    app.run(debug=True)