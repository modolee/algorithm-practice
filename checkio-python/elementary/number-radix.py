def checkio(str_number, radix):
    number_list = list(map(lambda x: int(x) if ord(x) < ord('A') else int(ord(x) - ord('A') + 10), str_number))

    if list(filter(lambda x: x >= radix, number_list)):
        return -1

    sum = 0;
    radix_index = len(number_list) - 1
    for i in range(0, len(number_list)):
        sum += number_list[i] * radix ** (radix_index - i)

    return sum