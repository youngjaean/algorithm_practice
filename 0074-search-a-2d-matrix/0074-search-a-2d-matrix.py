class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        left = 0
        right = n*m

        while left < right:
            mide = (left+right ) // 2
            r = mide // m
            c = mide % m
            if matrix[r][c] < target:
                left = mide+1
            elif matrix[r][c] > target:
                right = mide
            else:
                return True
            
        return False
            