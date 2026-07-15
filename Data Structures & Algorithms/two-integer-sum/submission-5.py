class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        filler = []
        output = []
        for i in range(len(nums)):
            required = target - nums[i]
            if required in nums[i+1:]:
                output.append(i)
                output.append(nums.index(required, i+1 if i < len(nums)-1 else i))
                return output
