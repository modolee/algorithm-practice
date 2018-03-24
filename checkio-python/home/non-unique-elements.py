def checkio(data):
    result = []

    for number in data:
        if data.count(number) > 1:
            result.append(number)

    return result