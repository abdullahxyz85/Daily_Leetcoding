from typing import List

import sys

# Increase max digit limit for string-to-int conversion
sys.set_int_max_str_digits(1000000)
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        result = []
        nums_str = []
        for i in num:
            i = str(i)
            nums_str.append(i)
        final_str = "".join(nums_str)

        sum_of_numbers = int(final_str) + k
        str_sum_of_numbers = str(sum_of_numbers)
        for i in str_sum_of_numbers:
            result.append(int(i))
        return result