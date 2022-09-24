# finding the maximum element from an unsorted array
def maximum(array):
    current_max = array[0]
    for i in range(1,len(array)):
        if current_max > array[i]:
            continue
        else:
            current_max = array[i]
    return current_max


def minimum(array):
    current_min = array[0]
    for i in range(1,len(array)):
        if current_min < array[i]:
            continue
        else:
            current_min = array[i]
    return current_min


print(maximum([8,9,4,1,3,2,10]))
print(minimum([8,9,4,1,3,2,10]))

def min_max(array,low,high):
    if len(array) == 1:
        return array

    elif len(array) == 2:
        if array[0] < array[1]:
            return (array[0],array[1])
        else:
            return (array[1],array[0])
    
    else:
        max = 0
        min = 0
        mid  = low+high//2
        array1 = min_max(array,low,mid)
        array2 = min_max(array,mid+1,high)

        # if lmax > rmax:
        #     max = lmax
        # else:
        #     max = rmax

        # if lmin < rmin:
        #     min = lmin
        # else:
        #     min = rmin

        # return (min,max)


print(min_max([8,9,4,1,3,2,10],0,6))

        
    














# 8 9 4 1 3 2 10
