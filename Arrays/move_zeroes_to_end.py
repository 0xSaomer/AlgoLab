def move_zeroes(nums):
    insert = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[insert] = nums[insert], nums[i]
            insert += 1

    return nums


print(move_zeroes([0,1,0,3,12]))

