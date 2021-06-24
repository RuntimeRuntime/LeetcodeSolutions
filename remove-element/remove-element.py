class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        startInc = 0
        endDec = -1
        nums.sort()
        for i in range(0, len(nums)):
            if val != nums[i]:
                #store nums[i] at position startInc
                nums[startInc] = nums[i]
                startInc += 1
        return startInc
                

        