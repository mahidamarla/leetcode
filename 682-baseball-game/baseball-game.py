class Solution:
    def calPoints(self, operations: list[str]) -> int:
        lst=[]
        for i in operations:
            if i!="+" and i!="D" and i!="C":
                lst.append(int(i))
            elif i=="+":
                a,b=lst[-1],lst[-2]
                lst.append(a+b)
            elif i=="D":
                val=lst[-1]*2
                lst.append(val)
            else:
                lst.pop()
        return sum(lst)