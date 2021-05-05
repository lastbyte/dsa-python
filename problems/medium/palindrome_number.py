
def palindrome_number( num : int) -> bool:
    if num < 0 :
        return False
    if int(str(num)[::-1]) == num:
        return True
    return False

print(palindrome_number(121))
print(palindrome_number(-121))