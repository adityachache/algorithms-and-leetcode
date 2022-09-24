class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        minNum = 6000
        
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            
            mid = (low+high)//2
            
            if nums[mid] < minNum:
                minNum = nums[mid]
                
            # if we are in right sorted portion then we need to check the left side of the array
            # [6,7,0,1,2,4,5] 
            # [6,7,1,2,4,5]
            
            if nums[mid] <= nums[high]:      
                high = mid - 1

            # if we are in the left sorted portion then if element[high] < element[low] then we need to check the right portion
            else:      
                if nums[high] < nums[low]:
                    low = mid + 1
                else:
                    high = mid - 1
                           
        return minNum
        
        
       