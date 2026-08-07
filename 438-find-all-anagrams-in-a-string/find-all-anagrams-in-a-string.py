class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d={}
        for i in p:
            d[i]=d.get(i,0)+1
        n=len(p)
        d1={}
        left=0
        ans=[]
        for right in range(len(s)):
            d1[s[right]]=d1.get(s[right],0)+1
            if right>=n-1:
                if d1==d:
                    ans.append(left)
                d1[s[left]]-=1
                if d1[s[left]]==0:
                    d1.pop(s[left])
                left+=1
        return ans
        