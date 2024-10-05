from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        occurences = []
        for i in range(len(nums)):
            if k == nums[i]:
                occurences.append(i)

        if len(occurences) >= 2:
            return False
        elif len(occurences) == 1:
            length = occurences[0]+1
        else:
            length = occurences[1] - occurences[0]

        if length <= k:
            return True
        else:
            return False



solution = Solution()
print(solution.containsNearbyDuplicate([1,2,3,1,2,3], 2)) # Expected: True