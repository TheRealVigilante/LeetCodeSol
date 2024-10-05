class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        while n >=4:
            if n % 4 != 0:
                return False
            n /= 4
        if n == 1:
            return True