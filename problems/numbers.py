def fibonacci(n):
    return 0 if n == 1 else 1 if n == 2 else fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci1(n, a, b):
    return a if n == 1 else b if n == 2 else fibonacci1(n - 1, b, a + b)


def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


def factorial1(n, a):
    return a if n == 0 else factorial1(n - 1, n * a)


if __name__ == "__main__":
    print("4th fibonacci number is : " + str(fibonacci(4)))
    print("Factorial of 4 is " + str(factorial(4)))
    print("-------------- Tail Recursion --------------------")
    print("4th fibonacci number is : " + str(fibonacci1(4, 0, 1)))
    print("Factorial of 4 is " + str(factorial1(4, 1)))

