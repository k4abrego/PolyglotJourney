# O(1)
def is_even(n: int) -> bool: 
    #LSB (least significant bit) is 1, even: LSB is 0
    return(n & 1) == 0 

# O(1)
def turn_uneven(n: int) -> int: #next odd number or  the same number if it is already odd
    return n | 1

# O(log N) because we are shifting the bits of n to the right until n becomes 0
def count_one_bits(n: int) -> int:
    count: int = 0
    while n:
        count += (n & 1)
        n >>= 1
    return count    


if __name__ == '__main__':
    print(f'{is_even(4) = }')
    print(f'{is_even(13) = }')
    print(f'{is_even(666) = }')
    print(f'{is_even(665) = }')
    print()
    print(f'{turn_uneven(4) = }')
    print(f'{turn_uneven(13) = }')
    print(f'{turn_uneven(666) = }')
    print(f'{turn_uneven(665) = }')
    print()
    print(f'{count_one_bits(5) = }')
    print(f'{count_one_bits(8) = }')
    print(f'{count_one_bits(7) = }')
