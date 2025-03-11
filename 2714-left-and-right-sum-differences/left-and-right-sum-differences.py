class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        totalSum = sum(nums)  # Step 1: Find total sum of the array
        leftSum = 0  # Initial left sum is 0
        answer = []

        # Step 2: Compute answer in a single loop
        for i in range(n):
            rightSum = totalSum - leftSum - nums[i]  # Compute rightSum dynamically
            answer.append(abs(leftSum - rightSum))  # Store absolute difference
            leftSum += nums[i]  # Update leftSum for the next index

        return answer
