from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            for j in range(len(arr)):  # Fix: Start from 0
                if i != j and (arr[i] == 2 * arr[j] or arr[j] == 2 * arr[i]):  # Fix: Correct condition
                    return True
        return False
