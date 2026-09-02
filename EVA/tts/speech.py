from pathlib import Path

import pyttsx3


def text_to_speech(text, output_dir, filename):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"{filename}.wav"

    engine = pyttsx3.init()
    engine.setProperty("rate", 165)
    engine.save_to_file(text, str(output_path))
    engine.runAndWait()
    engine.stop()

    if not output_path.exists() or output_path.stat().st_size == 0:
        raise RuntimeError("Text-to-speech audio could not be generated.")

    return output_path
