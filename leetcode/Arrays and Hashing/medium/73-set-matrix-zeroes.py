class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        indexList = {}  # O(n) space
    
        rowToZero = {} # O(m) space

        for j in range(len(matrix)):
            for i in range(len(matrix[j])):  # O(m*n) time

                if matrix[j][i] == 0:
                    if i not in indexList:
                        indexList[i] = 0
                    if j not in rowToZero:
                        rowToZero[j] = 0

        for index in indexList:              # O(n*m) time
            for j in range(len(matrix)):
                if j in rowToZero:
                    continue
                else:
                    matrix[j][index] = 0


        for row in rowToZero:       # O(m) time
            matrix[row] = [0] * len(matrix[row])
                
        