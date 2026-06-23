class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp=nums
        temp.sort()
        for k in range(1,len(nums)):
            if temp[k-1]==temp[k]:
                return True
        return  False
        