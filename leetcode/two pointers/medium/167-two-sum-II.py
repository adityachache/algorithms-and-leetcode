class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l = 0
        r = len(numbers) - 1
    
        while l<r:
            addsum = numbers[l] + numbers[r]
            if addsum == target:
                return [l+1, r+1]
            # if addsum is greater than target that means we need to decrement the right pointer because the 
            # array is sorted in increasing order (large numbers will always towards the end of the array)
            elif addsum > target:
                r -= 1
            # if addsum is less than target that means we need to increment the left pointer because the 
            # array is sorted in increasing order (small numbers will always be towards the beginning of the array)
            elif addsum < target:
                l += 1
