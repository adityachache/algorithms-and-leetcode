class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # Most efficient solution O(logn + logm)

        # perform a binary search on matrix to determine in which row the element belongs
        low = 0
        high = len(matrix) - 1

        arrayInd = 0

        while low <= high:

            mid = (low+high)//2

            if target > matrix[mid][0] and target < matrix[mid][-1]:
                arrayInd = mid
                break

            elif target < matrix[mid][0]:
                high = mid -1

            elif target > matrix[mid][-1]:
                low = mid + 1

            elif target == matrix[mid][0] or target == matrix[mid][-1]:
                return True

        # perform binary search again on the found row in the matrix
        newArr = matrix[arrayInd]

        return self.binarySearch(newArr, target)
        
             
    
    def binarySearch(self, arr, target):
        
        low = 0
        high = len(arr) - 1
        
        while low <= high:
            
            mid = (low+high)//2
            
            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                high = mid - 1
            elif arr[mid] < target:
                low  = mid + 1
            
        return False