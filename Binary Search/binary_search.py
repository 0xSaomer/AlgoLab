class BinarySearch:
    def search(self, nums, target):
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2  # find the middle number
            if nums[mid] == target:
                return mid  # target is found

            elif nums[mid] < target:
                low = mid + 1  # Target is on the left side

            else:
                high = mid - 1

        return None


result = BinarySearch()
print(result.search(nums=[2, 3, 5, 6, 7, 8], target=6))
