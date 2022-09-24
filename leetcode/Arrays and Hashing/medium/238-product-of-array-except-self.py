class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # O(N) and with using division operator
        product = 1
        mylist = []
        count = 0
    
        for i in nums:
            if i!= 0:
                product *= i
            else:
                count += 1
            
        if count == 0:
            for i in range(len(nums)):
                mylist.append(int(product/nums[i]))
     
        # if there is one zero in the array then the place where the zero is will be replaced by the product of all elements           except zero and rest all elements will be zero
        elif count == 1:     
            for i in range(len(nums)):
                if nums[i] == 0:
                    mylist.append(product)
                else:
                    mylist.append(0)
                    
                    
        # if there is more than one zero in the array then all elements in resulting array will be zero
        else:
            for i in range(len(nums)):
                mylist.append(0)
    
        return mylist
        