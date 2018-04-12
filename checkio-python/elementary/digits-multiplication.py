from functools import reduce
def checkio(number):
    return reduce(lambda x,y:x*y, filter(lambda x: x >0, map(lambda x:int(x), str(number))))