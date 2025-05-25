class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        max_result = ""

        for i in range(len(number)):
            if number[i] == digit:
                # Build new string manually without using slicing
                new_number = ""
                for j in range(len(number)):
                    if j != i:
                        new_number += number[j]
                if new_number > max_result:
                    max_result = new_number

        return max_result
