def fib(n):
    """Return the n-th Fibonacci Number."""
    if n == 1 or n == 2:
        return n-1
    a = 0
    b = 1
    i = 0
    for i in range(n-2):
        a, b = b, a+b
    return b

def fib1(n):
    """Return the n-th Fibonacci Number."""
    if n == 1 or n == 2:
        return n-1
    else:
        return fib(n-2) + fib(n-1)
