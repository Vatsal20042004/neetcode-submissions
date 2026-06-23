class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            temp = False
            s_dict={}
            for i in s:
                if i in s_dict:
                    s_dict [i]+=1
                else:
                    s_dict[i]=1
            t_dict={}
            for _ in t:
                if _ in t_dict:
                    t_dict[_]+=1
                else:
                    t_dict[_]=1
            if t_dict == s_dict:
                temp = True
        return temp
