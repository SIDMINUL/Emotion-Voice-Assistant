import numpy as np
import soundfile as sf


def _load_audio(path):
    y, sr = sf.read(path, always_2d=False)
    y = np.asarray(y, dtype=np.float32)
    if y.ndim > 1:
        y = np.mean(y, axis=1)
    y = np.nan_to_num(y)
    return y, sr


def extract_features(path):
    """Extract lightweight audio features without librosa/numba."""
    y, sr = _load_audio(path)

    if y.size == 0 or sr <= 0:
        return {"pitch": 0.0, "energy": 0.0}

    energy = float(np.sqrt(np.mean(np.square(y))))

    # Estimate dominant pitch from the FFT in the human voice range.
    window = y[: min(len(y), sr * 5)]
    window = window * np.hanning(len(window))
    spectrum = np.abs(np.fft.rfft(window))
    freqs = np.fft.rfftfreq(len(window), d=1.0 / sr)
    mask = (freqs >= 50) & (freqs <= 300)
    pitch = float(freqs[mask][np.argmax(spectrum[mask])]) if np.any(mask) else 0.0

    return {"pitch": pitch, "energy": energy}
