def between_markers(text: str, begin: str, end: str) -> str:
    initial = text.find(begin)
    if initial != -1:
        initial += len(begin)
    else:
        initial = 0

    final = text.find(end)
    if final == -1:
        final = len(text)

    if final < initial:
        return ''
    else:
        return text[initial:final]