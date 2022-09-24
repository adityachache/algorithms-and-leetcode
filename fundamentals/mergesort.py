def mergesort(arr):
    if len(arr) == 1:
        return arr
    else:
        mid = len(arr)//2
        left_arr  = arr[:mid]
        right_arr = arr[mid:]
        print(f'left array {left_arr}')
        print(f'right array {right_arr}')
        return merge(mergesort(left_arr),mergesort(right_arr))

def merge(left_arr,right_arr):
    results = []
    left_index = 0
    right_index = 0
    while (left_index < len(left_arr)) and (right_index < len(right_arr)):
        if (left_arr[left_index] < right_arr[right_index]):
            results.append(left_arr[left_index])
            left_index += 1
        else:
            results.append(right_arr[right_index])
            right_index += 1

    return results + left_arr[left_index:] + right_arr[right_index:]     

print(mergesort([1,5,7,3,8,2,76,32]))
