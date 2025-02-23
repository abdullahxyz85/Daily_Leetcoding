class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)  # Get the size of the array
        result = [0] * n  # Initialize the result array

        for i in range(n):
            if nums[i] == 0:
                result[i] = 0  # Directly assign zero
            else:
                new_index = (i + nums[i]) % n  # Compute new index
                result[i] = nums[new_index]  # Assign the new value

        return result

