PHI: float = 2/ (5 ** 0.5 -1)
#complexity:
#   Time = (PHI ^ n)|
#   Space = O(n)

def fibo_v1(n:int) -> int:
    if n <= 1:
        return n
    else:
        return fibo_v1(n-1) + fibo_v1(n-2)

#complexity:
#   Time = O(n)
#   Space = O(1)
def fibo_v2(n:int) -> int:
    a: int = 0
    b: int = 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a

#complexity:
#   Time = O(1)
#   Space = O(1)

def fibo_v3(n:int) -> int:
    return round((PHI ** n - (-1/PHI) ** n) / (5 ** 0.5))

if __name__ == '__main__':
    prev: int = 1
    for i in range(1, 42):
        result: int = fibo_v1(i)
        print(f'fibo_v1({i}) = {result/prev}')
        prev = result
        print(f'PHI = {PHI}')
