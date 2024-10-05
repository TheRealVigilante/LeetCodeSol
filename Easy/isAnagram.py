class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        length = len(s)
        t = sorted(t)
        length2 = len(t)
        if length != length2:
            return False
        if s == t:
            return True
        else:
            return False


sol = Solution()
print(sol.isAnagram("anagwam", "nagaram"))