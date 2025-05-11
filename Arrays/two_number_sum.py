def two_number_sum(nums, target):
    # Use two pointers to find a pair of numbers that sum up to the target.
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        # If the target sum is found, return the pair.
        if current_sum == target:
            return [nums[left], nums[right]]
        # Move the left pointer rightward to increase the sum.
        if current_sum < target:
            left += 1
        else:
            # Move the right pointer leftward to decrease the sum.
            right -= 1

    # Return None if no valid pair is found.
    return None


print(two_number_sum(nums=[1, 2, 3, 4, 5, 6, 7, 8, 9], target=9))