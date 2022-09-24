class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myhash = {}
        for key,value in enumerate(nums):
            if (target-value) in myhash:
                return [myhash[target-value], key]
            else:
                myhash[value] = key