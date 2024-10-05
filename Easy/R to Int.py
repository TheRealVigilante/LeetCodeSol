class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {' ': 0,'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0
        s = s+" "
        cont = True
        for i in range(len(s)):
            print(s[i])
            if s[i] == "I" and s[i+1] == "V":
                num += 4
                cont = False
                continue
            elif s[i] == "I" and s[i+1] == "X":
                num += 9
                cont = False
                continue
            elif s[i] == "C" and s[i+1] == "M":
                num += 900
                cont = False
                continue
            elif s[i] == "C" and s[i+1] == "D":
                num += 400
                cont = False
                continue
            elif s[i] == "X" and s[i+1] == "L":
                num += 40
                cont = False
                continue
            elif s[i] == "X" and s[i+1] == "C":
                num += 90
                cont = False
                continue
            elif i < len(s) and s[i] == "I":
                num += 1
            elif cont:
                num += roman_dict[s[i]]
            cont = True
        return num

sol = Solution()
print(sol.romanToInt("IX"))