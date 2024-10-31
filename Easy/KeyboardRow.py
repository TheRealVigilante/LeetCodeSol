from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        for word in words:
            for row in rows:
                if all([c.lower() in row for c in word]):
                    yield word
                    break


sol = Solution()
print(list(sol.findWords(["Hello", "Alaska", "Dad", "Peace"])))
