def checkio(words):
    splitedWords = words.split(' ')

    count = 0
    for word in splitedWords:
        if word.isdigit():
            count = 0
        else:
            count += 1

        if count == 3:
            return True

    return False