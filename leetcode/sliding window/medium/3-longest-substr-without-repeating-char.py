class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
           
        longest = 1
        curr = 1

        i = 0
        j = 1
        
        if len(s) == 0:
            return 0

        # add first char to hashtable
        myhash = {s[0]: 0}

         # loop from 2nd char
        while j < len(s):

            # if char is unique add it to hash
            if s[j] not in myhash:
                myhash[s[j]] = 0
                curr += 1
                # take the longest substring
                longest = max(longest, curr)
                j += 1
    
            # if char is duplicate then increment pointers and reset hashtable
            else:
                curr = 1
                i += 1
                j = i+1 
                myhash = {s[i]: 0}

        return longest