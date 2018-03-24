def str(t):
    return t[0]

def cnt(t):
    return t[1]

def checkio(text):
    dict = {}
    tuples = []

    for i in range(0, len(text)):
        if text[i].isalpha():
            if text[i].lower() in dict:
                dict[text[i].lower()] += 1
            else:
                dict[text[i].lower()] = 1
    for item in dict.items():
        tuples.append(item)

    tuples.sort(key=str)
    tuples.sort(key=cnt, reverse=True)

    print(tuples)

    return tuples[0][0]