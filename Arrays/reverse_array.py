# This function reverses a given array of integers
def reverse_array(array):
    left, right = 0, len(array) - 1
    while left < right:
        array[left], array[right] = array[right], array[left]

        left += 1
        right -= 1

    return array

print(reverse_array(array=[1,2,3,4,5,6]))
