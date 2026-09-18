class Solution:
    def removeDuplicates(self, s: str) -> str:
        lst=[]
        for i in s:
            if not lst:
                lst.append(i)
            else:
                if lst[-1]==i:
                    lst.pop()
                else:
                    lst.append(i)       
        return "".join(lst)
        