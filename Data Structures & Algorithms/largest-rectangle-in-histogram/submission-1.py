class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        from collections import deque
        stack=deque()
        k=0
        max_area=0
        for i in range(len(heights)):
            k=i

            while stack and stack[-1][0]>heights[i]:
                k=stack[-1][1]
                area=(i-k)*stack[-1][0]
                max_area=max(max_area,area)
                stack.pop()
            
            stack.append((heights[i],k))
        
        end=len(heights)
        while stack:
            area=stack[-1][0]*(end-stack[-1][1])
            max_area=max(max_area,area)
            stack.pop()
        return max_area


        