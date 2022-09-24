# 2 arrays are given and we need to find the common element in both of them
# for eg array1 = ['a','h','u','t'] and array2 = ['f','x','u','h']
# so we should return true for this since the element 'h' is common in both arrays

# simple approach O(n^2) complexity if array size are same otherwise its O(a*b) 
# def common_element(arr1,arr2):
#     for i in arr1:
#         for j in arr2:
#             if i == j:
#                 return True

# print(common_element(['a','h','u','t'],['f','x','k','p']))

def common_element(arr1,arr2):
    myhash = {}
    for index,value in enumerate(arr1):
        myhash[value] = index
    for i in arr2:
        if i in myhash:
            return True
    return False
print(common_element(['a','h','u','t'],['f','x','k','l']))