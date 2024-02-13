def isPalindrome(x: int) -> bool:

    if x < 0:
        return False
    
    # Calculate multiple
    multiple: int = 1
    while x >= multiple * 10:
        multiple *= 10

    while x:

        left: int = x // multiple
        right: int = x % 10

        if left != right:
            return False


        # Get the remainder (Gets rid of the first digit)
        x = x % multiple

        # Get the floor of this division (Gets rid of the last digit)
        x = x // 10

        multiple = multiple / 100
    
    return True


print(isPalindrome(1))