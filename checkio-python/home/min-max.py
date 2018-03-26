def min(*args, **kwargs):
    key = kwargs.get("key", None)
    min_list = []
    if len(args) == 1:
        for arg in args[0]:
            min_list.append(arg)
    elif len(args) > 1:
        for arg in args:
            min_list.append(arg)
    min_list.sort(key=key)
    return min_list[0]


def max(*args, **kwargs):
    key = kwargs.get("key", None)
    max_list = []
    if len(args) == 1 :
        for arg in args[0] :
            max_list.append(arg)
    elif len(args) > 1 :
        for arg in args :
            max_list.append(arg)
    max_list.sort(key=key, reverse=True)
    return max_list[0]