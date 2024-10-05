class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum(map(ord, t)) - sum(map(ord, s)))

sol = Solution()
print(sol.findTheDifference("abcd", "andcb"))