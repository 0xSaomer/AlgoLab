def minMax(array):
    # Initialize pointers at both ends of the list
    left, right = 0, len(array) - 1
    new_list = []

    # Loop while left index is less than right index
    while left < right:
        # Append the current max (right) and min (left) to the result list
        new_list.append(array[right])
        new_list.append(array[left])
        # Move inward from both ends
        left += 1
        right -= 1

    return new_list


print(minMax([1, 2, 3, 4, 5, 6]))
