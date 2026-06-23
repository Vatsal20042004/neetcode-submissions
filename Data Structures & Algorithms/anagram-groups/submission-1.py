class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res={}
        for i in strs:
            ch = [0]*26
            for j in i:
                ch[ord(j)-ord('a')]+=1
            key=tuple(ch)
            if key in res:
                res[key].append(i)
            else:
                res[key]=[i]
        result=[]
        for keys in res:
            result.append(res[keys])
        
        return result
        
        


        