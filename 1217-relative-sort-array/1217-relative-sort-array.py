from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # Step 1: Make a frequency count of elements in arr1
        count = []
        for i in range(1001):  # since 0 <= arr1[i] <= 1000
            count.append(0)
        
        for i in range(len(arr1)):
            count[arr1[i]] = count[arr1[i]] + 1

        result = []

        # Step 2: First add elements from arr2 in correct order
        for i in range(len(arr2)):
            num = arr2[i]
            while count[num] > 0:
                result.append(num)
                count[num] = count[num] - 1

        # Step 3: Add remaining elements in increasing order
        for num in range(1001):
            while count[num] > 0:
                result.append(num)
                count[num] = count[num] - 1

        return result
