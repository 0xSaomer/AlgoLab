# This function calculates the factorial of a given N integer
def factorial(n):
    if n == 1 or n == 0:
        return n

    return n * factorial(n-1)


print(factorial(5))