# This function calculates the given N integer of a Fibonacci sequence
def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(8))
