class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        # Step 1: Sort the array to bring negatives to the front
        nums.sort()
        
        # Step 2: Flip the most negative numbers first
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1  # Reduce the flip count
        
        # Step 3: If k is still > 0, flip the smallest number (if k is odd)
        if k % 2 == 1:
            nums.sort()  # Sort again to find the smallest number
            nums[0] = -nums[0]  # Flip the smallest number
        
        # Step 4: Return the sum of the modified array
        return sum(nums)
