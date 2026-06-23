class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff={}
        for i in range(len(nums)):
            diff[target-nums[i]]=i
        for i in range(len(nums)):
            if nums[i] in diff and diff[nums[i]]!=i:
                return sorted([i,diff[nums[i]]]) 