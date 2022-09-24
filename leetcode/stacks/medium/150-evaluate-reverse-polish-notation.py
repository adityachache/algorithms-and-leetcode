class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
              
        for i in tokens:
            
            if i == '+':
                first = stack.pop()
                second = stack.pop()
                
                exp = second + first
                stack.append(exp)
            
            elif i == '-':
                first = stack.pop()
                second = stack.pop()
                
                exp = second - first
                stack.append(exp)
                
            elif i == '*':
                first = stack.pop()
                second = stack.pop()
                
                exp = second * first
                stack.append(exp)
                
            elif i == '/':
                first = stack.pop()
                second = stack.pop()
                
                exp = second / first
                stack.append(int(exp))
            
            else:
                stack.append(int(i))
                
        
        return stack[0]