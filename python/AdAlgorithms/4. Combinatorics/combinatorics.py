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

 #in combinations the order doesn't matter
def combinations[T] (s: list[T], k: int) -> list[list[T]]:
    return [t for t in power_set(s) if len(t) == k]

#in permutations the order matters
# insert (7, [1, 2, 3], 0) -> [7, 1, 2, 3]
# insert (7, [1, 2, 3], 1) -> [1, 7, 2, 3]
def insert[T] (x: T, s:list[T], i: int) -> list[T]:
    return s[:i] + [x] + s[i:] # the + operator concatenates lists, so we are creating a new list with x inserted at index i

def insert_everywhere[T] (x: T, s: list[T]) -> list[list[T]]:
   return [insert (x, s, i) for i in range(len(s) + 1)]     

def permute[T] (s: list[T]) -> list[list[T]]:
    if not s:
        return [[]]
    empty: list[list[T]] = []
    return sum([insert_everywhere(s[-1], e) for e in permute(s[:-1])], empty) # Recursively call permute excluding the last element
    #return sum([insert_everywhere(s[:-1], e) for e in permute(s[:-1])], [])

if __name__ == "__main__":
    # pprint(power_set([])) #type: ignore
    # pprint(power_set([1])) 
    # pprint(power_set(['a', 'b']))
    # pprint(nicely_sorted(power_set(['a', 'b', 'c'])))
    # pprint(nicely_sorted(power_set(['a', 'b', 'c', 'd'])))
    # pprint(sorted(combinations([1, 2, 3, 4], 3)))
    # pprint(sorted(combinations([1, 2, 3, 4], 0)))
    # pprint(insert(7, [1, 2, 3], 3))
    # pprint(insert(7, [1, 2, 3], 0))
    # pprint(insert_everywhere(7, [1, 2, 3, 4, 5, 6]))
    pprint(permute([1, 2]))