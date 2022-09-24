class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        for i in range(len(s)):
        
            first = s[0]
            s = s[1:] + first

            if s == goal:
                return True
        
        return False