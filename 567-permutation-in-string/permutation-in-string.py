class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d2={}
        for i in s1:
            d2[i]=d2.get(i,0)+1
        d1={}
        left=0
        k=len(s1)
        ans=[]
        for right in range(len(s2)):
            d1[s2[right]]=d1.get(s2[right],0)+1
            if right>=k-1:
                if d1==d2:
                    return True
                d1[s2[left]]-=1
                if d1[s2[left]]==0:
                    d1.pop(s2[left])
                left+=1
        else:
            return False
