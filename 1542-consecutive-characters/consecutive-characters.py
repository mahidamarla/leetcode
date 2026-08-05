class Solution:
    def maxPower(self, s: str) -> int:
        count=1
        maxcount=1
        i=1
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                count+=1
            else:
                maxcount=max(maxcount,count)
                count=1
        return max(maxcount,count)