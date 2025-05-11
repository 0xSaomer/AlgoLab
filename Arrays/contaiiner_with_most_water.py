class Container_with_most_water:
    def Container(self, nums):
        # Initialize two pointers at the start and end of the list
        left, right = 0, len(nums) - 1
        max_waters = 0

        # Loop until the two pointers meet
        while left < right:
            width = right - left  # Distance between the two lines
            height = min(nums[left], nums[right])  # Container height is limited by the shorter line
            area = height * width  # Calculate the area (water held)
            max_waters = max(max_waters, area)  # Update max area if current one is larger

            # Move the pointer with the shorter line to potentially find a taller one
            if nums[left] < nums[right]:
                left += 1
            else:
                right -= 1

        return max_waters


sol = Container_with_most_water()
print(sol.Container([2, 3, 4, 5, 6, 7, 9]))
