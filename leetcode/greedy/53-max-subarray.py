def maxSubArray(nums):

    # ***Kadan's Algorithm O(n)***

    curr_sum = 0
    # condition to check if all elements are non positive 
    max_sum = float("-inf")
    
            
    # condition to check if array contains only one element
    if len(nums) == 1:
        return nums[0]
    else:
        for i in nums:
            curr_sum = max(i, curr_sum+i)
            max_sum = max(curr_sum, max_sum)
        return max_sum
        


    # ***Brute Force Approach O(n3)***

    # arr = []
    # # [-5,-3,-2,-1,1,1,2,4,4]
    # Sum = 0
    # ptr1 = 0
    # ptr2 = len(nums)
    # while ptr1 < len(nums):
    #     while ptr2 > ptr1:
    #         for i in range(ptr1, ptr2):
    #             Sum += nums[i]
    #         ptr2 -= 1
    #         arr.append(Sum)
    #         Sum = 0
    #     ptr1 += 1
    #     ptr2 = len(nums)

    # return max(arr)


result = maxSubArray([1,2,-4,-7,3,6,5])
print(result)

            
        