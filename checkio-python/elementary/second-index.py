def second_index(text: str, symbol: str):
    if text.count(symbol) <= 1:
        return None
    else:
        idx = text.index(symbol) + 1
        return idx + text[idx:].index(symbol)

    return 0