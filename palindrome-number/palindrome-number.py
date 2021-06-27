class Solution:
    def isPalindrome(self, x: int) -> bool:
        j = -1
        # convert x to string
        nums = str(x)
        # i goes from start to first half, j goes from end to send half
        for i in range(0, math.ceil(len(nums)/2)):
            if nums[i] != nums[j]: return 0
            j -= 1
        return 1