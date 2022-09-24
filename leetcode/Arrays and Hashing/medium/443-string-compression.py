class Solution:
    def compress(self, chars: List[str]) -> int:
        
        s = ""
        count = 1
        
        if len(chars) == 1:
            return 1
   
        for i in range(len(chars)-1):       
            if chars[i] == chars[i+1]:
                count += 1
            else:
                if count == 1:
                    s += chars[i]
                else:
                    s += chars[i] + str(count)                
                count = 1
          
        
        if count == 1:
            s += chars[-1]
        else:
            s += chars[-1] + str(count)
        
        
        for i in range(len(s)):
            chars[i] = s[i]    
        for i in range(len(chars)-1, (len(s)-1), -1):
            chars.pop()
        
        return len(chars)
        