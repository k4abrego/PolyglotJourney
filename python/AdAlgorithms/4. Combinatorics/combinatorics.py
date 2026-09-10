from pprint import pprint
from typing import cast

# Complexity: O(2^n) where n is the length of the input list
def power_set[T](s: list[T]) -> list[list[T]]:
    if not s:
        return [[]]
    temp: list[list[T]] = power_set(s[:-1]) # Recursively call power_set excluding the last element
    return temp + [e + [s[-1]] for e in temp]

if __name__ == "__main__":
    pprint(power_set([])) #type: ignore
    pprint(power_set([1])) 
    pprint(power_set([1, 2]))
    pprint(power_set([1, 2, 3]))