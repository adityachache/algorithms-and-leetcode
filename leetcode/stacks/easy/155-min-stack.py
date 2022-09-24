class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')
        self.min_arr = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.min = float('inf') 
        if val <= self.min:
            self.min = val
            self.min_arr.append(val)
        self.stack.append(val)  

    def pop(self) -> None:
        if self.stack[-1] == self.min_arr[-1]:
            self.min_arr.pop()
            if self.min_arr:
                self.min = self.min_arr[-1]
            else:
                self.min = float('inf') 
        self.stack.pop()

        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min
    


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()



# ["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
# [[],[1],[1],[2],[],[],[],[],[],[],[2],[],[],[3],[],[],[],[]]