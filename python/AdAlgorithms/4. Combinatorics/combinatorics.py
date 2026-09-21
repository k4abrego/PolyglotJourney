from pprint import pprint
from typing import cast

def nicely_sorted[T] (s: list[T]) -> list[list[T]]:
    def size_and_content(value: list[T]) -> tuple[int, list[T]]:
        return(len(value), value)

        
        return sorted(s, key= size_and_content) #for using a key you just nedd to add a tuple of the size


# Complexity: O(2^n) where n is the length of the input list
def power_set[T](s: list[T]) -> list[list[T]]:
    if not s:
        return [[]]
    temp: list[list[T]] = power_set(s[:-1]) # Recursively call power_set excluding the last element
    return temp + [e + [s[-1]] for e in temp]


def combinations[T] (s: list[T], k: int) -> list[list[T]]:
    return [t for t in power_set(s) if len(t) == k]

if __name__ == "__main__":
    # pprint(power_set([])) #type: ignore
    # pprint(power_set([1])) 
    # pprint(power_set(['a', 'b']))
    # pprint(nicely_sorted(power_set(['a', 'b', 'c'])))
    # pprint(nicely_sorted(power_set(['a', 'b', 'c', 'd'])))
    pprint(sorted(combinations([1, 2, 3, 4], 3)))