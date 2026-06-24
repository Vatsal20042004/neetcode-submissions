class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]*len(nums)
        sufix=[1]*len(nums)
        result=[]

        for i in range(1,len(nums)):
            prefix[i]=prefix[i-1]*nums[i-1]
        for j in range(len(nums)-2,-1,-1):
            sufix[j]=sufix[j+1]*nums[j+1]
        
        print(prefix)
        print(sufix)
        for i in range (len(nums)):
            result.append(prefix[i]*sufix[i])
        
        return result

        


        