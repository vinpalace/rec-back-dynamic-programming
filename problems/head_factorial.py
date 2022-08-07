def factorial(n):

    if n == 0:
        return 1

    res1 = factorial(n - 1)
    res2 = n * res1

    return res2


print(factorial(10))
