class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        t_hash = {}
        for ch in t:
            t_hash[ch] = t_hash.get(ch, 0) + 1

        s_hash = {}

        required = len(t_hash)
        formed = 0

        start = 0
        min_len = float('inf')
        res = ""

        for end in range(len(s)):

            if s[end] in t_hash:
                s_hash[s[end]] = s_hash.get(s[end], 0) + 1

                if s_hash[s[end]] == t_hash[s[end]]:
                    formed += 1

            while formed == required:

                if end-start+1 <min_len:
                    min_len=end-start+1
                    res=s[start:end+1]

                if s[start] in t_hash:
                    s_hash[s[start]]-=1

                    if s_hash[s[start]]<t_hash[s[start]]:
                        formed -= 1

                start += 1

        return res