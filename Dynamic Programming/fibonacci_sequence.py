# This function calculates the given N integer of a Fibonacci sequence
def fibonnaci(n):
    if n <= 1:
        return n

    return fibonnaci(n-1) + fibonnaci(n-2)


print(fibonnaci(8))
