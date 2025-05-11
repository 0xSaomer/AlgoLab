# This function returns the first non-repeating integer in the given list
# It uses a dictionary (hash_map) to track the frequency of each element
# Then it loops through the list again to find the first element with a frequency of 1

def firstNonRepeatingInteger(nums):
    # Create a hashmap (dictionary) to store the frequency of each element
    hash_map = {}

    # Loop through the elements and count their occurrences in the hashmap
    for i in nums:
        if i in hash_map:
            # If the number is already in the hashmap, increment its count
            hash_map[i] += 1
        else:
            # If the number is not in the hashmap, add it with count 1
            hash_map[i] = 1

    # Loop through the list again to find the first element with count 1 (non-repeating)
    for j in nums:
        if hash_map[j] == 1:
            # Return the first non-repeating number
            return j

    # If all elements repeat, return None
    return None


# Example usage
print(firstNonRepeatingInteger(nums=[2, 3, 2, 1, 4, 5, 3, 1]))  # Output: 4
