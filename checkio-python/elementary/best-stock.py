def best_stock(data):
    max_key = ''
    max_value = 0
    for key in data:
        if data[key] > max_value:
            max_key = key
            max_value = data[key]

    return max_key