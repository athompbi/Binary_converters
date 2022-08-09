#### given a binary number, convert to a decimal

def binary_to_decimal(binary):

    binary = str(binary)
    decimal = 0

    index = -1
    multiple = 0

    for i in binary:

        if binary[index] == '1':
            decimal += 2 ** multiple
        index -= 1
        multiple += 1

    return decimal


### given a decimal number, convert to binary

### find how many bits are needed to create the number

print(binary_to_decimal(11011))


# import math

# decimal = 5

# binary = []

# bits_needed = int(math.log(decimal,2) + 1)

# for i in range(bits_needed):
#     binary.append(0)

# print(binary)

# for i in binary:
#     mult = bits_needed - 1
#     print(f'i = {i}')
#     print(f'mult = {mult}')
#     print(f'2^mult = {2 ** mult}')
#     print(f'remaining decimal = {decimal}')

#     if 2 ** mult <= decimal:
#         decimal -= 2 ** (bits_needed - 1)
#         binary[i] = 1
#         print(binary[i])
#         bits_needed -= 1
#     else:
#         bits_needed -= 1
#         print(binary[i])

# print(binary)

"""
1 = 1
2 = 10
3 = 11
4 = 100
5 = 101
6 = 110
7 = 111
8 = 1100
9 = 1001
10 = 1010
11 = 1011
12 = 1100
13 = 1101
14 = 1110
15 = 1111
16 = 10000
17 = 10001
18 = 10010
19 = 10011
20 = 10100
21 = 10101
22 = 10110
23 = 10111
24 = 11000
25 = 11001
26 = 11010
27 = 11011
"""




