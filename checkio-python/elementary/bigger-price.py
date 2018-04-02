def bigger_price(limit, data):
    sorted_list = sorted(data, key=lambda x: x['price'], reverse=True)
    return sorted_list[:limit]