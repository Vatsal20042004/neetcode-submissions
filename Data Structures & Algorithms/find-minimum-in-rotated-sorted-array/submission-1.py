class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0]<nums[-1]:
             return nums[0]
        
        min_ele=nums[0]
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            min_ele=min(min_ele,nums[mid])

            if nums[mid]<nums[right]:
                right=mid-1
            else:
                left=mid+1
        
        return min_ele
            

        
    
        