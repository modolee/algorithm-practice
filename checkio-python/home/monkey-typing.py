def count_words(text, words):
    count = 0;
    for word in words:
        if text.lower().find(word) != -1:
            count += 1

    return count