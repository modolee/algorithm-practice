def first_word(text: str) -> str:
    no_word = [' ', '.', ',']

    start_idx = 0
    while text[start_idx] in no_word:
        start_idx += 1

    end_idx = start_idx
    while (text[end_idx] not in no_word):
        end_idx += 1
        if end_idx == len(text):
            return text[start_idx:]

    return text[start_idx:end_idx]