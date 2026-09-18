class Solution:
    def isValid(self, s: str) -> bool:
        open_b="{[("
        close_b="}])"
        d=dict(zip(close_b,open_b))
        lst=[]
        for i in s:
            if i in open_b:
                lst.append(i)  
            else:
                if not lst:
                    return False
                else:
                    if d[i]==lst[-1]:
                        lst.pop()
                    else:
                        return False
        return not lst

