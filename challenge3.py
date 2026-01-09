def check_palindrome(str):
    if str==str[::-1]:
        return True
    else:
        return False
def longest(str):
    if str[0]==str[-1]:
        if check_palindrome(str):
            return len(str)
        else:
            return 0


    else:
        left = longest(str[1:])
        right = longest(str[:-1])

        if (left) > (right):
            return (left)
        else:
            return (right)

print(longest("geeks"))

