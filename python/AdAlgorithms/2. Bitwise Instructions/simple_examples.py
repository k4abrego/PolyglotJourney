a: int = 5      # 0b0101
b: int = 9      # 0b1001
c: int = 15     # 0b1111

print(f'{a = }')
print(f'{b = }')
print(f'{c = }')

print(f'{bin(a) = }')
print(f'{oct(b) = }')
print(f'{hex(c) = }')

s: str = '1010'
print(f'{int(s) = }')
print(f'{int(s, 2) = }')
print(f'{int(s, 8) = }')
print(f'{int(s, 10) = }')
print(f'{int(s, 16) = }')
print(f'{int(s, 36) = }') #36 is the maximum base allowed. 0-9 A-Z
print(f'{int("zz", 36) = }') #35^z * 36^1 + 35^z * 36^0 = 1295

print(f'{a & b = }') # bitwise AND
print(f'{a & c = }')
print(f'{b & c = }') 
print()
print(f'{a | b = }') # bitwise OR
print(f'{a | c = }') 
print(f'{b | c = }') 
print()
print(f'{a ^ b = }') # bitwise XOR
print(f'{a ^ c = }') 
print(f'{b ^ c = }')
print()
print(f'{~a = }') # bitwise NOT
print(f'{~b = }')
print(f'{~c = }')

