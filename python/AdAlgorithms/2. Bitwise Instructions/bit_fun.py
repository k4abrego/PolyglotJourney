# O(1)
def is_even(n: int) -> bool: 
    #LSB (least significant bit) is 1, even: LSB is 0
    return(n & 1) == 0 

def turn_uneven(n: int) -> int: #next odd number or  the same number if it is already odd
    return n | 1
    

if __name__ == '__main__':
    print(f'{turn_uneven(4) = }')
    print(f'{turn_uneven(13) = }')
    print(f'{turn_uneven(666) = }')
    print(f'{turn_uneven(665) = }')
