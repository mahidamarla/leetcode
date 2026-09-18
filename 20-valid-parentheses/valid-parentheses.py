class Solution:
    def isValid(self, s: str) -> bool:
        open_b="{[("
        close_b="}])"
        lst=[]
        for i in s:
            if i in open_b:
                lst.append(i)  
            else:
                if not lst:
                    return False
                else:
                    if i == ")" and lst[-1] == "(" or i == "}" and lst[-1] == "{" or i == "]" and lst[-1] == "[" :
                        lst.pop()
                    else:
                        return False
        return not lst

