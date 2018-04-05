from functools import reduce
def find_message(text):
    return reduce(lambda x,y: x+y, list(map(lambda x : x if x.isupper() == True else '', text)))