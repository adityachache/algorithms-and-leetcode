class Solution:
    def isValid(self, s: str) -> bool:
        
        
        # Initialize an empty stack
        stack = []
        
        # loop over the string
        for char in s:
            
            # if we find any opening bracket then we push it on the stack
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
                
            # This statement only gets triggered when the string starts with closing bracket eg: },),]
            elif not stack:
                return False
            
            # if we find any closing bracket after pushing to the stack we check if it's equal to the last pushed char
            # if it is we pop it off the stack if not then we return False
            elif char == ')' and stack[-1] == '(':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()
            elif char == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return False
            
            
        # in the end if all closing brackets are found then stack will be empty
        return len(stack) == 0
     
        
        # '([]){}'