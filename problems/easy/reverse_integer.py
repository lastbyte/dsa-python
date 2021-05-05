def reverse_integer(num : int) -> int :
    if num == 0 or int ( str(abs(num))[::-1]) > pow(2, 31) :
        return 0;
    return ( num // abs(num) ) * int ( str(abs(num))[::-1])

print(reverse_integer(1563847412))
print(reverse_integer(-120))