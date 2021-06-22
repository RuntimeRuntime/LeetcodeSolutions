class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        #initialise numbers dictionary to {keys: 0 ....}
        numbers = dict.fromkeys(nums, 0)
        for i in range(0, len(nums)):
            #incrament the value corresponding to the key with value nums[i] 
            numbers.update({nums[i]: int(numbers.get(nums[i], None)) + 1})
        #convert numbers to a list, then get numbers[numbers value with index 1]
        return list(numbers.keys())[list(numbers.values()).index(1)]
        