from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        print(mat)
        if len(mat) * len(mat[0]) != r * c:
            return mat
        else:
            flat = [item for sublist in mat for item in sublist]
            res = []
            for i in range(r):
                res.append(flat[i*c:(i+1)*c])
            return res


sol = Solution()
print(sol.matrixReshape([[1, 2], [3, 4]], 1, 4))
print(sol.matrixReshape([[1, 2], [3, 4]], 2, 4))