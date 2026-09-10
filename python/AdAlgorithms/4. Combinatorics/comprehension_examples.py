from pprint import pprint
from typing import Iterator

print([2**n for n in range (100) if 2**n < 100])

#comprehension is to reduce lines of code
#example of a list comprehension
result: list[int] = []
for n in range(100):
    if 2**n < 100:
        result.append(2**n)

print(result)

#Example set comprehension
print({c.upper() for c in 'Hello, World!' if c not in ' , !'})

#Example dictionary comprehension
#key-colon-associated value
print({n: 2** n for n in range (11)})

#yield creates a generator 
#Example of a generator comprehension
g: Iterator[int] = (2**n for n in range(1_000_000_000))
print(next(g)) #lazy sequence, only produce the next value one at a time
print(next(g))
print(next(g))
for i in g:
    if i > 100:
        break
    print(i)


#if we use more than one for we wolud produce a partition product (Cartesian product)

a: list[int] = [1, 2]
b: list[str] = ['a', 'b', 'c']
pprint([(x, y) for x in a for y in b]) #Cartesian product


pprint([(x, y, z) for x in range(2) for y in range(2) for z in range(2)])



pprint([(a, b, c) for a in range(1, 101)
                  for b in range(1, 101)
                  for c in range(1, 101)
                  if a < b < c <= 100 and a**2 + b**2 == c**2 ])

