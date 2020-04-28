class MinStack:

    def __init__(self):
        self.container=[]
        self.minStack=[sys.maxsize]
        self.minStackSize = 1

    def push(self, x: int) -> None:
        self.container.append(x)
        if x<=self.minStack[self.minStackSize-1]:
            self.minStack.append(x)
            self.minStackSize+=1
        
    def pop(self) -> None:
        x = self.container.pop()
        if self.minStack[self.minStackSize-1]==x:
            self.minStackSize-=1
            self.minStack.pop()
        return x

    def top(self) -> int:
        return self.container[-1]
        
    def getMin(self) -> int:
        return self.minStack[self.minStackSize-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
