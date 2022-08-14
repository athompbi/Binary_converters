def binary_to_decimal(binary):
    """Converts a binary number to a decimal
    
    Return:
        decimal: converted number"""

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




import math

def decimal_to_binary(decimal):
    """Converts a number in decimal to a binary number
    
    Return:
        binary: converted number"""

    bits_needed = int(math.log(decimal,2) + 1)

    binary = []

    for i in range(bits_needed - 1, -1, -1):
        if decimal >= 2 ** i:
            binary.append('1')
            decimal -= 2 ** i
        else:
            binary.append('0')

    binary = ''.join(binary)

    return binary




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




