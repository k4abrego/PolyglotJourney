def g(n: int) -> int:
    r = 1
    for _ in range(n):
        r <<= 1
    return r

def f(n: int) -> int:
    r = 0
    t = g(n)
    for _ in range(1, t):
        r += 1
    return r

# O(1)
def f(n: int) -> int:
    return (1 << n) - 1
 
print(f(0))
print(f(1))
print(f(2))
print(f(5))
print(f(10))
