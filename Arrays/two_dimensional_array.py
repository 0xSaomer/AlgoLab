def diagonal_and_reverse_diagonal(array):
    # Get the length of the array (assuming it's a square matrix)
    length = len(array)

    # Initialize empty lists for the diagonals
    diagonal = []
    reversed_diagonal = []

    # Loop through the array to collect diagonals
    for i in range(length):
        diagonal.append(array[i][i])  # Main diagonal element
        reversed_diagonal.append(array[i][length - i - 1])  # Reverse diagonal element

    return diagonal, reversed_diagonal


array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


print(diagonal_and_reverse_diagonal(array))
