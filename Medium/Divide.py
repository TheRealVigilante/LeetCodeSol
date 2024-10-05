

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        if dividend == 0:
            return 0
        if divisor == 1:
            return dividend
        if divisor == -1:
            return -dividend
        sign = 1
        if dividend < 0:
            sign = -sign
            dividend = -dividend
        if divisor < 0:
            sign = -sign
            divisor = -divisor
        res = 0
        while dividend >= divisor:
            temp = divisor
            multiple = 1
            while dividend >= temp:
                dividend -= temp
                res += multiple
                multiple += multiple
                temp += temp
        return res if sign == 1 else -res