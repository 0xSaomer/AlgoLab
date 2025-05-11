class BinarySearch:
    def SearchPosition(self, nums, target):
        # crate two pointers
        low, high = 0, len(nums) - 1


        while low <= high:
            # create a while loop
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid # return target if found

            elif nums[mid] < target:
                low = mid + 1 # if target less than mid, move low to the right

            else:
                high = mid -1 # if mid bigger than target, move high to the left

        return low


sol = BinarySearch()
print(sol.SearchPosition(nums=[1, 2, 4, 5, 7, 8], target=3))
