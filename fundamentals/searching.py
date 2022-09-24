# LINEAR SEARCH
def linear_search(arr,num):
    for i in range(len(arr)):
        if arr[i] == num:
            return f"element found at {arr.index(arr[i])}"
    return False

# print(linear_search([1,2,3,4,5],7))



# works for a sorted array
# BINARY SEARCH ITERATIVE
def binary_search_iterative(arr,num,low,high):
    while high >= low:
        mid = (low+high)//2
        if arr[mid] == num:
            return f"element found at index {mid}"
        elif num > arr[mid]:
            low = mid + 1
        else:
            high = mid -1
    return False
  
    

array = [1,2,3,4,5]
num = 1
# print(binary_search_iterative(array,num,0,len(array)-1))


# BINARY SEARCH RECURSIVE
def binary_search_recursive(arr,num,low,high):
    if high >= low:
        mid = (low+high)//2
        if arr[mid] == num:
            return f"element found at index {mid}"
        elif arr[mid] < num:
            return binary_search_recursive(arr,num,mid+1,high)
        else:
            return binary_search_recursive(arr,num,low,mid-1)
    else:
        return False

# print(binary_search_recursive(array,num,0,len(array)-1))