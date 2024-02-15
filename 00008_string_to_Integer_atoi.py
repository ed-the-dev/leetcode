def myAtoi(s: str) -> int:

    result: int = 0
    numbers_started: bool = False
    is_negative: bool = False

    def return_result(result: int, is_negative: bool) -> int:

        if is_negative:
            result = result * -1

        if result < -2147483648:
            return -2147483648
        
        if result > 2147483647:
            return 2147483647
        
        return result

    for index, character in enumerate(s):

        if character == ' ' and not numbers_started:
            continue

        if (character == '-') and not numbers_started:

            if (index+1) < len(s) and s[(index+1)].isdigit():
                is_negative = True
                continue
            else:
                return return_result(result, is_negative)

        if (character == '+' and not numbers_started):
            if (index+1) < len(s) and s[(index+1)].isdigit():
                continue
            else:
                return return_result(result, is_negative)

            

        if character.isdigit():
            result = (result * 10) + int(character)
            numbers_started = True
        else :
            return return_result(result, is_negative)

    return return_result(result, is_negative)
        
print(myAtoi('2a42'))