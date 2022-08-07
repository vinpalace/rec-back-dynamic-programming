def tail_factorial(n, accumulator=1):

    if n == 1:
        return accumulator

    return tail_factorial(n - 1, n * accumulator)


print(tail_factorial(10))

# This is much better because of tail recursion, they are independent stack
# frames.
# next stack frame is not dependent on caller frame.
# even though python doesnt optimize this much, other languages can optimize
# it.
