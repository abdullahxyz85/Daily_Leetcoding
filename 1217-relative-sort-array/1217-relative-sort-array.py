from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = []
        for i in range(1001):  
            count.append(0)
        
        for i in range(len(arr1)):
            count[arr1[i]] = count[arr1[i]] + 1

        result = []

        for i in range(len(arr2)):
            num = arr2[i]
            while count[num] > 0:
                result.append(num)
                count[num] = count[num] - 1

        for num in range(1001):
            while count[num] > 0:
                result.append(num)
                count[num] = count[num] - 1

        return result
