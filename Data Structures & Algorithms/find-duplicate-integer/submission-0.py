class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        res = [0]*(n)
        for ele in nums:
            if res[ele] == 1:
                return ele
            else:
                res[ele] = 1
        
        