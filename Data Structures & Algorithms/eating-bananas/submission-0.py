class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        left=1
        right=max(piles)
        res=right

        while left<=right:
            mid=(left+right)//2
            k=0

            for num in piles:
                k+=math.ceil(num/mid)
            
            if k<=h:
                res=min(res,mid)
                right=mid-1
            else:
                left=mid+1
                
        return res


        