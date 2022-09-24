class Solution:
   
    
    def romanToInt(self, s: str) -> int:
        
        symbol_table = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        int_num = 0
        previous = 0
        
        for i in range(len(s)-1,-1,-1):
            if symbol_table[s[i]] >= previous:
                int_num += symbol_table[s[i]]
            else:
                int_num -= symbol_table[s[i]]
                
            previous = symbol_table[s[i]]
            
        return int_num
            


        