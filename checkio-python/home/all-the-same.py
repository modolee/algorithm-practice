from typing import List, Any

def all_the_same(elements: List[Any]) -> bool:
    if len(elements) == 0 :
        return True
    else:
        return (len(elements) == elements.count(elements[0]))