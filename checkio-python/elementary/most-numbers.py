def checkio(*args):
    if (len(args) == 0):
        return 0

    arg_list = list(args)
    arg_list.sort()

    return float(arg_list[len(arg_list) - 1]) - float(arg_list[0])