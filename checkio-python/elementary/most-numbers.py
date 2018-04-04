def checkio(*args):
    if(len(args) == 0) :
        return 0
    else :
        return max(args) - min(args)