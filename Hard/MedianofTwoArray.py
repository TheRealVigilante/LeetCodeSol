from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        final_list = sorted(nums1 + nums2)
        print(final_list)
        listlen = len(final_list)
        if listlen % 2 == 0:
            median = (final_list[listlen//2] + final_list[listlen//2 - 1]) / 2
        else:
            median = final_list[listlen//2]
        return round(median,5)


sol = Solution()
print(sol.findMedianSortedArrays([1, 3], [2, 4]))