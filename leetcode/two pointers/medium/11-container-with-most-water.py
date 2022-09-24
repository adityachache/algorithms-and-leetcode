class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max_size = 0
        curr_size = 0
        
        l = 0
        r = len(height) - 1
              
        while l < r:
            
            # calculate the area according to the formula
            curr_size = min(height[l], height[r]) * (r-l)
            max_size = max(max_size, curr_size)
            
            
            # we need to consider line with greater height 
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return max_size
            
            
            