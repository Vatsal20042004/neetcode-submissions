class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        res=0
        for i in nums:
            if (i-1) not in num_set:
                length=1
                while (i+length) in num_set:
                    length+=1
                res=max(res,length)
        return res


        