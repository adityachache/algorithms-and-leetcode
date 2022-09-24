def bubblesort2(array):
    length = len(array)
    for i in range(0,length):
        for j in range(0,length-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
            
    return array

# print(bubblesort2([1,2,5,8,3,4,65,32,48]))
# print(bubblesort2(['b','n','j','q','a','y','c']))

def selection_sort(arr):
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j] < arr[i]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr
# print(selection_sort(['b','n','j','q','a','y','c']))
# print(selection_sort([1,2,5,8,3,4,65,32,48]))

def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
print(insertion_sort(['b','n','j','q','a','y','c']))
print(insertion_sort([1,2,5,8,3,4,65,32,48]))