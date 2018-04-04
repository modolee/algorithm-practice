def checkio(number):
    answer = ''
    if number % 3 == 0:
        answer += 'Fizz'
        if number % 5 == 0:
            answer += ' Buzz'
    elif number % 5 == 0:
        answer += 'Buzz'
    else:
        answer += str(number)

    return answer