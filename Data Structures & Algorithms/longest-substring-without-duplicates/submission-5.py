class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length=0
        substring={}
        start=0
        for i in range(len(s)):
            if s[i] in substring and substring[s[i]]>=start:
                start=substring[s[i]]+1
            substring[s[i]]=i
            length=max(length,i-start+1)

        return length
        