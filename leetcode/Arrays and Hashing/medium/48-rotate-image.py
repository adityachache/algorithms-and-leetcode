class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        i = 0
        j = len(matrix) - 1
    
        while i <= j:
            matrix[i],matrix[j] = matrix[j], matrix[i]
            i += 1
            j -= 1
        

        j = 2
        for x in range(len(matrix)-1,-1,-1):
            i = 1
            for y in range(len(matrix[x])-j,-1,-1):
                matrix[x][y], matrix[x-i][y+i] = matrix[x-i][y+i], matrix[x][y]
                i += 1
            j += 1

        return matrix