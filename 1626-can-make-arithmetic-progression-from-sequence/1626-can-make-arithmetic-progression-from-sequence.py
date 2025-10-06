class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool: 
        sorted_arr = sorted(arr)  # sort the array first, e.g., [1, 3, 5]
        difference = sorted_arr[1] - sorted_arr[0]  # find the first difference

        # check all consecutive differences
        for i in range(2, len(sorted_arr)):
            if sorted_arr[i] - sorted_arr[i - 1] != difference:
                return False  # if any difference is not same, return False

        return True  # if loop completes, all differences are equal → True
