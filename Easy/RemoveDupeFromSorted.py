from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        return list(set(nums))


sol = Solution()
print(sol.removeDuplicates([1,1,2])) # 2