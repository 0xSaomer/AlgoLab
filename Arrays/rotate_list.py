class Rotatelist:
    def rotate(self, nums, k):
        # Calculate the split index where the list will be rotated
        choose_side = len(nums) - k

        # Slice the list into two parts: right (last k elements), left (remaining)
        right_side = nums[choose_side:]
        left_side = nums[:choose_side]

        # Concatenate right side first to complete the rotation
        return right_side + left_side


# Create an instance of the class and rotate the list by k positions
Rotate = Rotatelist()
rotate = Rotate.rotate(nums=[10, 20, 30, 40, 50], k=3)
print(rotate)
