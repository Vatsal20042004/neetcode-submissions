from collections import deque
from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = deque([])
        nge = [-1] * len(nums2)
        
        for i in range(len(nums2) - 1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if stack:
                nge[i] = stack[-1]                
            stack.append(nums2[i])
        n2 = {}
        for i in range(len(nums2)):
            n2[nums2[i]] = i
            
        nge_res = []
        for j in nums1:
            nge_res.append(nge[n2[j]])
            
        return nge_res
