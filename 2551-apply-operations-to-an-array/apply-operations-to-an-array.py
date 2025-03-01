class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Step 1: Apply the operations
        for i in range(n - 1):
            if nums[i] == nums[i + 1] and nums[i] != 0:
                nums[i] *= 2
                nums[i + 1] = 0

        # Step 2: Move all zeros to the end
        result = [num for num in nums if num != 0]  # Collect non-zero numbers
        result += [0] * (n - len(result))  # Append required number of zeroes

        return result
