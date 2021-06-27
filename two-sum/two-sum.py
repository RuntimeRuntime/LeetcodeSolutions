class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapNums = dict()
        # Loop through nums
        for i in range(0, len(nums)):
            goal = target - nums[i]
            # Does mapNums contain goal value?
            if goal in mapNums:
                # Return indexes of goal, and i
                return(mapNums.get(goal), i)
            # add (nums[i], i) to mapNums dictionary
            mapNums.update({nums[i]: i})
        return None
            