class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # O(NlogN) Time My approach
        if len(nums) == 0:
            return 0
        
        sorted_nums = sorted(nums)
    
        curr_len = 0
        max_len = 0
        i = 0
        j = 1
        
        
        while j < len(sorted_nums):
            
            # if next number is equal to 1 + previous number then it's consecutive
            if sorted_nums[j] == sorted_nums[i] + 1:
                curr_len += 1
                max_len = max(max_len,curr_len)
                
            # if both numbers are equal then dont do anything
            elif sorted_nums[j] == sorted_nums[i]:
                pass
            
            # if not consecutive then reset current length
            else:
                curr_len = 0

            i += 1
            j += 1

        # return max length + 1 because an array with single element will always be consecutive
        return max_len + 1

    
#         O(N) Time neetcode 
#         nums = set(nums)
        
#         longest = 0
        
#         for i in nums:
            
#             if (i-1) not in nums:
#                 length = 0
                
#                 while (i+length) in nums:
#                     length += 1
                
#                 longest = max(longest, length)
            
        
#         return longest
        
                    
        