class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
            
        # Actually got accepted even though it runs in O(M*N)
#         flag = False
#         counts1 = {}
    
#         for s in s1:
#             if s not in counts1:
#                 counts1[s] = 1
#             else:
#                 counts1[s] += 1

#         i = 0
#         j = len(s1) - 1

#         while j < len(s2):

#             newstr = s2[i:j+1]

#             counts2 = {}

#             for s in newstr:
#                 if s not in counts2:
#                     counts2[s] = 1
#                 else:
#                     counts2[s] += 1

#             if counts2 == counts1:
#                 flag = True
#                 break
#             else:
#                 flag = False

#             i += 1
#             j += 1

#         return flag



        # Neetcode O(N) Solution
    
        if len(s1) > len(s2): return False
        
        s1Count, s2Count = [0] *26, [0] * 26
        matches = 0
        
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
            
            
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
            
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: 
                return True
            
            index = ord(s2[r]) - ord('a') 
            s2Count[index] += 1     
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1
            
            index = ord(s2[l]) - ord('a') 
            s2Count[index] -= 1     
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
                
            l += 1
        
        return matches == 26
            
            
        