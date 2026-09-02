from pathlib import Path
import tempfile

from flask import Flask, jsonify, render_template, request

from audio.speech_to_text import transcribe
from models.emotion_model import detect_emotion
from models.policy_model import choose_action
from llm.response_generator import generate_response

BASE_DIR = Path(__file__).resolve().parent
AUDIO_DIR = BASE_DIR / "audio" / "generated"
AUDIO_DIR.mkdir(parents=True, exist_ok=True)

app = Flask(__name__, template_folder="templates")
app.config["MAX_CONTENT_LENGTH"] = 15 * 1024 * 1024

# Google speech recognition currently works with the WAV AudioFile path used
# by this deployment, so keep the cloud upload contract intentionally small.
ALLOWED_EXTENSIONS = {"wav"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify({"status": "ok", "service": "emotion-voice-assistant"})


@app.route("/process", methods=["POST"])
def process_audio():
    if "audio" not in request.files:
        return jsonify({"error": "No audio file was provided."}), 400

    file = request.files["audio"]
    if not file.filename:
        return jsonify({"error": "Please select a WAV audio file."}), 400
    if not allowed_file(file.filename):
        return jsonify({"error": "Please upload a WAV audio file."}), 400

    input_path = None
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav", dir=AUDIO_DIR) as temp_file:
            input_path = Path(temp_file.name)
            file.save(input_path)

        emotion = detect_emotion(str(input_path))
        action = choose_action(emotion)
        text = transcribe(str(input_path)).strip()

        if not text:
            return jsonify({"error": "I couldn't understand the audio. Please try again with a clearer recording."}), 422

        response = generate_response(text, emotion, action)

        return jsonify({
            "text": text,
            "emotion": emotion,
            "action": action,
            "response": response,
            "audio": None,
        })

    except Exception as exc:
        app.logger.exception("Audio processing failed")
        return jsonify({"error": f"Audio processing failed: {exc}"}), 500
    finally:
        if input_path and input_path.exists():
            input_path.unlink(missing_ok=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
