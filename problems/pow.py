'''
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
'''

def power(x: float , n: int) -> float:
    return x ** n

def power1(x: float , n: int) -> float:

    if n == 0:
        return 1

    if n%2 == 0:
        return power1(x, int(n/2)) * power(x, int(n/2))
    else:
        if n > 0:
            return x * power1(x, int(n/2)) * power1(x, int(n/2))
        else:
            return (power1(x, int(n/2)) * power1(x, int(n/2))) / x



print(power(2.10000,3))
print(power1(2.10000,3))

print(power(2,-3))
print(power1(2,-3))

