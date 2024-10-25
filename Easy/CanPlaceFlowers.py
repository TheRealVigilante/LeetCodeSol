from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0  # Tracks the number of flowers we can place
        length = len(flowerbed)

        for i in range(length):
            # Check if current plot is empty and adjacent plots are also empty or boundaries
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == length - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1  # Place a flower here
                count += 1
                if count >= n:  # If we've placed enough flowers, return True
                    return True

        # If we exit the loop without placing enough flowers
        return count >= n

sol = Solution()
print(sol.canPlaceFlowers([1,0,0,0,1],2))