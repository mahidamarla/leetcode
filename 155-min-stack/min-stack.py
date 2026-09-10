class MinStack:

    def __init__(self):
        self.st=[]
        self.mnstack=[]
    def push(self, value: int) -> None:
        self.st.append(value)
        if not self.mnstack:
            self.mnstack.append(value)
        else:
            self.mnstack.append(min(value,self.mnstack[-1]))
    def pop(self) -> None:
        self.mnstack.pop()
        return self.st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.mnstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()