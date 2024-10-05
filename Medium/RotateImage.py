from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        # Transpose the matrix
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


        # Reverse the matrix
        for i in range(len(matrix)):
            matrix[i].reverse()

sol = Solution()
print(sol.rotate([[1,2,3],[4,5,6],[7,8,9]]))