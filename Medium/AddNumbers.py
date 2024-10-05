from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> list[int]:
        strL1=""
        strL2=""

        for i in range(len(l1)):
            strL1+=str(l1[i])

        for i in range(len(l2)):
            strL2+=str(l2[i])

        total = int(strL1) +int(strL2)
        return [int(digit) for digit in str(total)]


sol = Solution()
print(sol.addTwoNumbers([2,4,3], [5,6,4]))