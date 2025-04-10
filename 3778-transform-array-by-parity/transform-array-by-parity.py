class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            if num % 2 == 0:
                result.append(0)
            else:
                result.append(1)
        sorted_result = sorted(result)
        return sorted_result