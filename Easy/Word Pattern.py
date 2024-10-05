class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        d = {}
        for i in range(len(pattern)):
            if pattern[i] in d:
                if d[pattern[i]] != s[i]:
                    return False
            else:
                if s[i] in d.values():
                    return False
                d[pattern[i]] = s[i]
        return True
sol = Solution()
print(sol.wordPattern("abba", "dog cat cat fish"))