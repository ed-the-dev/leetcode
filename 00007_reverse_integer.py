import math

def reverse( x: int) -> int:

    MAX: int = 2147483647
    MIN: int = -2147483648

    result: int = 0

    while x:
        # Required to calculate negative digits because -1 % 10 = 9
        digit: int = int(math.fmod(x, 10))

        # Required to calculate negative 'rest of number' because -1 // 10 = -1
        x = int(x / 10)

        # print('Result: %s' % result)
        # print('rest of number: %s' % x)
        # print('Digit: %s' % digit)

        # If the result is greater than all but the last digit of the MAX
        # or if it's equal to and the next number will push over the MAX, then return 0.
        if (result > MAX // 10 or (result == MAX // 10 and digit > MAX % 10)):
            return 0
        
        # If result is currently less than all but the last digit of MIN
        # or if it's equal to and the final number is less than -8, then return 0.
        if (result < int(MIN/10) or (result == int(MIN/10) and digit < int(math.fmod(MIN, 10)))):
            return 0
        
        result = (result * 10) + digit

    return result

print(reverse(-7463847412))
print(int(math.fmod(-2147483648, 10)))
