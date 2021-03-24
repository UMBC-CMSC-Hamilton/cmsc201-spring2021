number = 0b101010
print(number)
# python can't remember whether you told it the number in hex, dec, or binary.
# stores it in binary
# displays it in decimal

# converts it to binary (computer doesn't really understand the difference between binary of 42 and decimal of 42
# it stores everything as binary
# how did it know to keep it binary this time?
print(bin(number), type(bin(number)))


#  TYPE IS FORBIDDEN <-- I'M ALLOWED.
# it gives you a string because computers don't really understand decimal anyway.

def dec_to_bin(number):
    result = ''
    # edge case, what if the number is just 0, hmm...
    if not number:
        result += '0'

    while number:
        # fixed
        if number % 2:
            # result += 1 means result = result + '1'
            # what we want is result = '1' + result <-- can't use += here... :(
            result = '1' + result
        else:
            result = '0' + result
        number //= 2
    return '0b' + result


print(dec_to_bin(5))
print(dec_to_bin(6))  # uh oh, it's backwards ... fixed
print(dec_to_bin(42))
print(dec_to_bin(511))
print(dec_to_bin(532874))

print(0b111100011)
print(0b010001, 0b10001)
print(0b1010111)
print(0b001111011001010100001111010111011110)
print(0x3D950F5DE)


def dec_to_hex(number):
    """
        next time, calculate using this algorithm by hand Dec <-> Hex
        Binary <-> Hex (just use the chart)
        Binary -> Decimal (powers calculation)
        Decimal to Binary (you need this algorithm, mod-divide algorithm).


    :param number:
    :return:
    """
    result = ''
    # edge case, what if the number is just 0, hmm...
    if not number:
        result += '0'

    while number:
        if number % 16 <= 9:
            result = str(number % 16) + result
        elif number % 16 == 10:
            result = 'A' + result
        elif number % 16 == 11:
            result = 'B' + result
        elif number % 16 == 12:
            result = 'C' + result
        elif number % 16 == 13:
            result = 'D' + result
        elif number % 16 == 14:
            result = 'E' + result
        elif number % 16 == 15:
            result = 'F' + result
        number //= 16
    return '0x' + result


print(hex(32921), dec_to_hex(32921))
print(hex(0b10101010101), dec_to_hex(0b10101010101))
for i in range(256):
    print(hex(i), dec_to_hex(i))

# old style (mostly in C) ALL UPPER, modern languages less upper casey style, lower case.
print(0xABCD, 0xabcd)

