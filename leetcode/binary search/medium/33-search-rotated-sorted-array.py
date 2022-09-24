class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # for detailed explanation refer this video - https://www.youtube.com/watch?v=U8XENwh8Oy8
        
        low = 0 
        high = len(nums) - 1
        
        while low <= high:
            
            mid = (low+high)//2
            
            if nums[mid] == target:
                return mid
            
            
            if nums[mid] >= nums[low]:
                
                if target < nums[mid] and target < nums[low]:
                    low = mid + 1
                    
                elif target < nums[mid]:
                    high = mid - 1
                    
                else:
                    low = mid + 1
            else:
                
                if target > nums[mid] and target > nums[high]:
                    high = mid - 1
                    
                elif target > nums[mid]:
                    low = mid + 1
                
                else:
                    high = mid - 1
                           
        return -1