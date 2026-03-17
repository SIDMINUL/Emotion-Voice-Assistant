def choose_action(emotion):

    if emotion == "sad":
        return "high_empathy"

    if emotion == "angry":
        return "supportive"

    return "neutral"