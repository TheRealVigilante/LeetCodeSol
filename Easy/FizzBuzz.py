from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = []
        count = 1
        for i in range(n):
            if count % 3==0  and count% 5==0:
                output.append("FizzBuzz")
            elif count % 3==0 :
                output.append("Fizz")
            elif count % 5==0 :
                output.append("Buzz")
            else:
                output.append(str(count))
            count+=1
        return output


sol = Solution()
print(sol.fizzBuzz(15))
# print(1%3)