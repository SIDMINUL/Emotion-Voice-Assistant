import numpy as np
import soundfile as sf


def _load_audio(path):
    y, sr = sf.read(path, always_2d=False)
    y = np.asarray(y, dtype=np.float32)
    if y.ndim > 1:
        y = np.mean(y, axis=1)
    return np.nan_to_num(y), sr


def _estimate_pitch(y, sr):
    if len(y) < 2 or sr <= 0:
        return 0.0
    window = y[: min(len(y), sr * 5)]
    window = window * np.hanning(len(window))
    spectrum = np.abs(np.fft.rfft(window))
    freqs = np.fft.rfftfreq(len(window), d=1.0 / sr)
    mask = (freqs >= 50) & (freqs <= 300)
    return float(freqs[mask][np.argmax(spectrum[mask])]) if np.any(mask) else 0.0


def _estimate_speaking_rate(y, sr):
    """Estimate speech activity events per minute from frame energy."""
    if len(y) < sr or sr <= 0:
        return 0.0

    frame = max(1, int(sr * 0.025))
    hop = max(1, int(sr * 0.010))
    energies = []
    for start in range(0, len(y) - frame, hop):
        chunk = y[start : start + frame]
        energies.append(np.sqrt(np.mean(chunk * chunk)))

    if not energies:
        return 0.0

    energies = np.asarray(energies)
    threshold = max(float(np.percentile(energies, 60)) * 1.15, 1e-4)
    active = energies > threshold
    starts = np.count_nonzero(active[1:] & ~active[:-1])
    duration_minutes = len(y) / sr / 60.0
    return float(starts / max(duration_minutes, 1 / 60.0))


def detect_emotion(audio_path):
    try:
        y, sr = _load_audio(audio_path)
        energy = float(np.sqrt(np.mean(np.square(y)))) if y.size else 0.0
        pitch = _estimate_pitch(y, sr)
        speaking_rate = _estimate_speaking_rate(y, sr)
    except Exception:
        # Emotion detection should never prevent transcription/response.
        return "neutral"

    print("Pitch:", pitch)
    print("Energy:", energy)
    print("Speaking rate:", speaking_rate)

    if energy < 0.02:
        return "sad"
    if pitch > 200 and energy > 0.04:
        return "angry"
    if speaking_rate > 180:
        return "excited"
    return "neutral"
