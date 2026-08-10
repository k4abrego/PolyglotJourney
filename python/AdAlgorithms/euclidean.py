def GCD(a: int, b:int) -> int:
    while True:
        r = int =a % b
        if r == 0:
            return b
        a, b = b, r

def comprimes(a: int, b: int) -> bool:
    return GCD(a, b) == 1

def gcd(a: int, b: int, *rest: int) -> int:
    result: int = GCD(a, b)
    for n in rest:
        result = GCD(result, n)
        return result

def lcm(a: int, b: int) -> int:
    return a * b // GCD(a, b)



if __name__ == '__main__':
    print(f'{GCD(20, 150) = }')
    print(f'{GCD(10, 666) = }')
    print(f'{GCD(666, 23) = }')
    print(f'{comprimes(666,23) = }')
    print(f'{comprimes(10, 666) = }')
    print(f'{gcd(20, 30, 40, 70, 100) = }')
    print(f'{gcd(60, 45) = }')
    print(f'{lcm(10, 20) = }')
    print(f'{lcm(15, 20) = }')




