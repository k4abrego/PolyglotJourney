def baby_methods(s:float, guess: float, delta: float) -> float:
    if s < 0:    
        raise ValueError(f'Cannot compute square root of: {s}')
    prev: float = guess
    while True:
        guess = (prev + s / prev) / 2
        if abs(guess - prev) <= delta:
            return guess
        prev = guess



if __name__ == '__main__':
    x: float = 30 
    result: float = baby_methods(30, 5, 0.0001)
    print(f'sqrt {x} = {result} ({result * result})')
