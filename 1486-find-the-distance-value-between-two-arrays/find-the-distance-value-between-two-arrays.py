class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0  # To count valid elements in arr1
        for num1 in arr1:
            valid = True  # Assume num1 is valid
            for num2 in arr2:
                if abs(num1 - num2) <= d:
                    valid = False  # num1 is not valid
                    break  # No need to check further
            if valid:
                count += 1  # Increase count if num1 is valid
        return count 