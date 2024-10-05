from typing import List
class Solution:
    def mergeTwoLists(self, list1: List, list2: List) -> List:
        current1 = list1
        current2 = list2
        print(current1)
        print(current2)
        current = []
        if current1 == [] and current2 == []:
            return []
        elif current1 == []:
            return current2
        elif current2 == []:
            return current1
        length1=len(current1)
        length2=len(current2)
        length=length1+length2
        j=0
        k=0
        cont = True
        for i in range(length):
            if not cont:
                cont = True
                continue
            if current1[j] < current2[k]:
                current.append(current1[j])
                j+=1
            elif current2[k] < current1[j]:
                current.append(current2[k])
                k+=1
            else:
                current.append(current1[j])
                current.append(current2[k])
                j+=1
                k+=1
                cont=False
        return current


sol = Solution()
print(sol.mergeTwoLists([1,2,4], [1,3,4]))