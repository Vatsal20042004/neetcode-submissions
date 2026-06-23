class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res={}
        for i in strs:
            temp="".join(sorted(i))
            if temp in res:
                res[temp].append(i)
            else:
                res[temp]=[i]
        
        final=[]
        for i in res:
            final.append(res[i])
        return final


        