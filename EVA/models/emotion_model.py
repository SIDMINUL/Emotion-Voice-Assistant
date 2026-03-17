import librosa
import numpy as np

def detect_emotion(audio_path):

    y, sr = librosa.load(audio_path, sr=None)

    # pitch
    pitch_values = librosa.yin(y, fmin=50, fmax=300, sr=sr)
    pitch = np.mean(pitch_values)

    # energy
    energy = np.mean(librosa.feature.rms(y=y))

    # speaking speed
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)

    print("Pitch:", pitch)
    print("Energy:", energy)
    print("Tempo:", tempo)

    if energy < 0.02:
        return "sad"

    elif pitch > 200 and energy > 0.04:
        return "angry"

    elif tempo > 140:
        return "excited"

    else:
        return "neutral"