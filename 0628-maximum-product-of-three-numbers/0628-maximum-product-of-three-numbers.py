class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()

        # Step 2: Get the product of the top 3 largest numbers
        product1 = nums[-1] * nums[-2] * nums[-3]

        # Step 3: Get the product of the 2 smallest numbers and the largest number
        product2 = nums[0] * nums[1] * nums[-1]

        # Step 4: Return the maximum of the two
        return max(product1, product2)