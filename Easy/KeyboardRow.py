from typing import List
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        result = []
        for word in words:
            for row in rows:
                if all([c.lower() in row for c in word]):
                    result.append(word)

        return result


sol = Solution()
print(list(sol.findWords(["Hello", "Alaska", "Dad", "Peace"])))
