class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        req={}
        for i in s1:
            req[i]=req.get(i,0)+1
        k=len(s1)
        sol={}
        length=0
        start=0
        for i in range(len(s2)):
            sol[s2[i]]=sol.get(s2[i],0)+1
            length+=1
            if length>k:
                if sol[s2[start]]==1:
                    del sol[s2[start]]
                else:   
                    sol[s2[start]]-=1
                start+=1
                length-=1
            if length==k and req==sol:
                return True
        return False



        