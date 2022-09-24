class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # O(N) neetcode approach
#         res = {}              
        
#         for s in strs:
            
#             count = [0]*26                 # making a list of 26 chars of english alphabets
            
#             for char in s:
                
#                 count[ord(char) - ord("a")] += 1        # update the count for each character in our string 
#                                                         # this count will be same for the words(tea, ate, eat)
                
#             if tuple(count) in res:
#                 # if count exists in dictionary then append the words 
#                 res[tuple(count)].append(s)             
#             else:
#                 # or else create a new list with the word at count
#                 res[tuple(count)] = [s]
        
            
#         return res.values()
    
    
        # O(nlogn) my approach
        res = {}
        
        for s in strs:
            
            sortedStr = ''.join(sorted(s))
            
            if sortedStr in res:
                res[sortedStr].append(s)
            else:
                res[sortedStr] = [s]
                
            
        return res.values()
    
    