def correct_sentence(text: str) -> str:
    return text[0].upper() + text[1:] + ('' if text.endswith('.') else '.')