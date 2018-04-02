def popular_words(text, words):
    dict = {}
    for word in words:
        dict[word] = text.lower().count(word)

    return dict