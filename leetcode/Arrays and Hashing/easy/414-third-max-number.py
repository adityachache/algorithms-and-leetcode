class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        sorted_nums = sorted(nums)
        count = 0
        max_num = sorted_nums[-1]
        
        for i in range(len(sorted_nums)-2,-1,-1):
            if sorted_nums[i] < max_num:
                max_num = sorted_nums[i]
                count += 1
                if count == 2:
                    return max_num
                
        return sorted_nums[-1]
                    
        
        
        # [-5,10,7,-8,3]