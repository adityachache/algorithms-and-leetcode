class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        myhash = {}
        
        for char in s:
            if char not in myhash:
                myhash[char] = 1
            else:
                myhash[char] += 1
            
            
        if len(s) != len(t):
            return False
    
        else:
            for letter in t:
                if letter not in myhash:
                    return False
                else:
                    myhash[letter] -= 1
                    if myhash[letter] < 0:
                        return False
            
            return True
        