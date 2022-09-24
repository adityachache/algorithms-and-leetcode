class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # O(nlogn) my approach
        myhash = {}
        # mylist = []
        
        for i in nums:
            if i in myhash:
                myhash[i] += 1
            else:
                myhash[i] = 1
        
        sorted_values = dict(sorted(myhash.items(), reverse=True, key=lambda x:x[1]))
        
        val_list = [key for key in sorted_values]
        
        return [val_list[i] for i in range(k)]