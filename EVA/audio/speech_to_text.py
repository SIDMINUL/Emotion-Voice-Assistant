import speech_recognition as sr


_recognizer = sr.Recognizer()


def transcribe(audio_path):
    """Transcribe a WAV recording using Google's public speech endpoint.

    This keeps the cloud deployment lightweight and avoids downloading a
    large Whisper model into a memory-constrained Render instance.
    """
    with sr.AudioFile(audio_path) as source:
        audio = _recognizer.record(source)

    try:
        return _recognizer.recognize_google(audio).strip()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError as exc:
        raise RuntimeError("Speech recognition service is temporarily unavailable.") from exc
