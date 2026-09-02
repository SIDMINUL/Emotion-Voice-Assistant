import os

from faster_whisper import WhisperModel

_model = None


def _get_model():
    global _model
    if _model is None:
        model_name = os.getenv("WHISPER_MODEL", "tiny")
        _model = WhisperModel(model_name, device="cpu", compute_type="int8")
    return _model


def transcribe(audio_path):
    model = _get_model()
    segments, _ = model.transcribe(audio_path, beam_size=1)
    return " ".join(segment.text.strip() for segment in segments).strip()
