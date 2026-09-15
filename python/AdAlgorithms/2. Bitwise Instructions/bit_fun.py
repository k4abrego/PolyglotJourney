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

# O(1) because we are using bitwise AND operation to check if n is a power of 2
def is_power_of_2(n:int)-> bool:
    return False if n <= 0 else (n -1) & n == 0

# O(log N) because we are shifting the bits of n to the right until n becomes 1 -----
def floor_log2(n : int) -> int:
    if n <= 0:
        raise ValueError(f'floor_log2 is not defined for{n}')
    result: int = 0
    while n > 1:
        result += 1
        n >>= 1
    return result

# O(log M) because we are shifting the bits of m to the right until m becomes 0
# def mul(m: int, n:int) -> int:
#     result: int = 0
#     while m:
#         result += n if (m & 1) else 0
#         m >>= 1
#         n <<= 1
#     return result

# # O(log min(m,n)) because we are shifting the bits of the smaller number to the right until it becomes 0
# def mul(m: int, n:int) -> int:
#     result: int = 0
#     if n < m:
#         n, m= m, n #swapping the values of n and m to reduce the number of iterations in the while loop
#     while m:
#         result += n if (m & 1) else 0
#         m >>= 1
#         n <<= 1
#     return result

def mul(m: int, n:int) -> int:
    negative: bool = (n < 0) ^ (m < 0) # check if the result should be negative xor operation to check if ONE of the numbers is negative
    m = abs(m)
    n = abs(n)
    result: int = 0
    if n < m:
        n, m= m, n 
    while m:
        result += n if (m & 1) else 0
        m >>= 1
        n <<= 1
    return -result if negative else result #if negative is true, return the negative of the result, else return the result

if __name__ == '__main__':
    # print(f'{is_even(4) = }')
    # print(f'{is_even(13) = }')
    # print(f'{is_even(666) = }')
    # print(f'{is_even(665) = }')
    # print(f'{turn_uneven(4) = }')
    # print(f'{turn_uneven(13) = }')
    # print(f'{turn_uneven(666) = }')
    # print(f'{turn_uneven(665) = }')
    # print(f'{count_one_bits(5) = }')
    # print(f'{count_one_bits(8) = }')
    # print(f'{count_one_bits(7) = }')
    # print(f'{is_power_of_2(8) = }')
    # print(f'{is_power_of_2(64) = }')
    # print(f'{is_power_of_2(7) = }')
    # print(f'{is_power_of_2(1) = }')
    # print(f'{is_power_of_2(255) = }')
    # print(f'{is_power_of_2(256) = }')
    # print(f'{is_power_of_2(0) = }')
    # print(f'{is_power_of_2(-5) = }')
    # print(f'{floor_log2(8) = }')
    # print(f'{floor_log2(128) = }')
    # print(f'{floor_log2(10) = }')
    # print(f'{floor_log2(25) = }')
    try:
        print(f'{floor_log2(0) = }')
    except ValueError:
        print(f'{mul(13,17) = }')
        print(f'{mul(5,20) = }')
        print(f'{mul(7, 0) = }')
        print(f'{mul(0, 7) = }')
        print(f'{mul(-5, 10) = }')
        print(f'{mul(13, -17) = }')
        print(f'{mul(-13, 17) = }')
        print(f'{mul(-13, -17) = }')


