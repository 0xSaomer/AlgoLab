# check if a string or an integer is a palindrome
class ValidPalindrome:
    def palindrome(self, nums):
        if isinstance(nums, int):
            nums = str(nums)
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] != nums[right]:
                return False
            left += 1
            right -= 1
        return True


sol = ValidPalindrome()
print(sol.palindrome(nums="racecar"))
print(sol.palindrome(nums='tst'))
print(sol.palindrome(nums=1213))