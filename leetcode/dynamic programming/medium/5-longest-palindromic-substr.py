class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_substr = ''
        max_len = 0
        
        # taking an element and expanding outwards
        for i in range(len(s)):
            
            # odd length palindromic substrings eg: "babab"
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > max_len:
                    max_len = (right - left + 1)
                    max_substr = s[left:right+1]
                
                left -= 1
                right += 1
                
                
            # even length palindromic substrings eg: "ceec"
            left = i
            right = i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > max_len:
                    max_len = (right - left + 1)
                    max_substr = s[left:right+1]
                    
                left -= 1
                right += 1
                
        return max_substr