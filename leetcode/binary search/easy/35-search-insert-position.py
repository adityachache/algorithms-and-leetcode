class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # binary search O(log n)
        
        low = 0
        high = len(nums) - 1
           
        
        while low <= high:
            
            mid = (low+high)//2 
            
            if nums[mid] == target:
                return mid
            
            elif target > nums[mid]:
                low = mid + 1
            
            elif target < nums[mid]:
                high = mid - 1
                
        return low
            
                
        
        
#         for i in range(len(nums)):
            
#             # if number at i == target return i if it's greater still return i cause that's where we would've inserted
#             if nums[i] >= target:
#                 return i
#             # if all numbers are less than target we would've inserted the target at the end
#             elif target > nums[-1]:
#                 return len(nums)
            
            
            