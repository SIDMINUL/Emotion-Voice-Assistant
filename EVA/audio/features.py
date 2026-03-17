import librosa
import numpy as np

def extract_features(path):

    y, sr = librosa.load(path, sr=None)

    pitch_values = librosa.yin(
        y,
        fmin=50,
        fmax=300,
        sr=sr
    )

    pitch = np.mean(pitch_values)

    energy = np.mean(librosa.feature.rms(y=y))

    return {
        "pitch": pitch,
        "energy": energy
    }