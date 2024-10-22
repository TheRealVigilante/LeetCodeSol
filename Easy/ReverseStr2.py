class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s_list = list(s)

        for i in range(0, len(s), 2 * k):
            # Reverse the first k characters in this block
            s_list[i:i + k] = reversed(s_list[i:i + k])

        return ''.join(s_list)

sol = Solution()
print(sol.reverseStr("abcdefg", 2))