class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        results = []
        for i in range(n):
            results.append(nums[i])
            results.append(nums[i + n])
        return results