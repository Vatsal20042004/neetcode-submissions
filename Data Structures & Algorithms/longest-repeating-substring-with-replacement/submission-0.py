class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq={}
        start=0
        max_freq=0
        length=0
        for end in range(len(s)):
            freq[s[end]]=freq.get(s[end],0)+1

            max_freq=max(max_freq,freq[s[end]])

            if (end-start+1)-max_freq>k:
                freq[s[start]]-=1
                start+=1
            length=max(length,(end-start+1))

        return length

        