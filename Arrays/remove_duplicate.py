def remove_duplicates(nums):
    # Pointer for the last unique element
    i = 0

    # Iterate through the list starting from the second element
    for j in range(1, len(nums)):
        # Check if the current element is different from the last unique one
        if nums[j] != nums[i]:
            i += 1  # Move the unique index forward
            nums[i] = nums[j]  # Update it with the new unique value

    # Return the number of unique elements
    return i + 1


nums = sorted([1, 2, 3, 1, 2, 4])
length = remove_duplicates(nums)
print(nums[:length])
