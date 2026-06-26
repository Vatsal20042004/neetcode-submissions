class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area=0
        left=0
        right=len(heights)-1

        while left<right:
            temp=min(heights[left],heights[right])*(right-left)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
            area = max(temp,area)
        return area

        