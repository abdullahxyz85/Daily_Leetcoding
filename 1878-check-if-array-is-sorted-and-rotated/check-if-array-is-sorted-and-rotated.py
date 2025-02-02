class Solution:
    def check(self, nums: List[int]) -> bool:
        count_breaks = 0  # To count the number of breaks

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:  # Check if there is a break
                count_breaks += 1

        # Check the last element with the first one (for rotation case)
        if nums[-1] > nums[0]:  
            count_breaks += 1

        return count_breaks <= 1  # True if at most one break exists
