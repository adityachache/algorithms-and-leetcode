class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
       
        # Monotonic stack neetcode O(N)
        
        # intialize our results array with zeroes
        res = [0] * len(temperatures)
        
        stack = []
        
        for i,v in enumerate(temperatures):
            
            while stack and v > stack[-1][1]:
                stackInd, stackVal = stack.pop()
                res[stackInd] =  i - stackInd
                
            stack.append([i,v])
            
        return res
    
    
    
    
        
#         O(N^2) doesn't work on leetcode (time limit exceeded)
#         res = []

#         i = 0
#         j = 1

#         while j < len(temperatures):

#             if temperatures[j] <= temperatures[i]:
#                 try:
#                     while temperatures[j] <= temperatures[i]:
#                         j += 1
#                     res.append(j-i)
#                 except:
#                     res.append(0)

#             else:
#                 res.append(j-i)

#             i += 1
#             j = i+1



#         res.append(0)
#         return res


        