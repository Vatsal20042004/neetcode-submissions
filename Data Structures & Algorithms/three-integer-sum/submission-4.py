class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        for j in range(len(nums)):
            if j>0 and nums[j]==nums[j-1]:
                continue
            a_1=j+1
            a_2=len(nums)-1
            target=-nums[j]
            while a_1<a_2:
                if nums[a_1]+nums[a_2]==target:
                    if [nums[a_1],nums[a_2],nums[j]] not in result:
                        result.append([nums[a_1],nums[a_2],nums[j]])
                    a_1+=1
                    a_2-=1
                    if nums[a_1]==nums[a_1-1]:
                        a_1+=1
                    if nums[a_2]==nums[a_2+1]:
                        a_2-=1
                elif nums[a_1]+nums[a_2]>target:
                    a_2-=1
                else:
                    a_1+=1
       
        return result


        