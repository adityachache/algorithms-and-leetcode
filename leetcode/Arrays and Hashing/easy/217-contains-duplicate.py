class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        myhash = {}
        
        for num in nums:
            if num in myhash:
                return True
            else:
                myhash[num] = 0
            
        return False
            

      