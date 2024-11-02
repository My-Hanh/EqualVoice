from openai import OpenAI

openai_api_key = "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"


BIAS_SURROUNDING_CHAR = "|"


# STUB data, remove when analyze is implemented

marked_text = f"The {BIAS_SURROUNDING_CHAR}cyclist's wife{BIAS_SURROUNDING_CHAR} won a gold medal.\n" + f"The {BIAS_SURROUNDING_CHAR}cyclist's wife{BIAS_SURROUNDING_CHAR} won a gold medal.\n" + f"The {BIAS_SURROUNDING_CHAR}cyclist's wife{BIAS_SURROUNDING_CHAR} won a gold medal."
global_feedback = "It looks great"


def analyze(user_text):
    # TODO
    return marked_text, global_feedback