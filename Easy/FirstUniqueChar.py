class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 0:
            return -1
        if len(s) == 1:
            return 0
        for i in range(len(s)):
            if s.count(s[i]) == 1:
                return i
        return -1