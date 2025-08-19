class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Step 1: Convert 0 → -1 so balance means sum = 0
        prefix_sum = 0
        # Dictionary to store first occurrence of prefix_sum
        prefix_map = {0: -1}   # important: prefix sum 0 seen at index -1
        max_length = 0

        # Step 2: Traverse the array
        for i, num in enumerate(nums):
            # treat 0 as -1, 1 as +1
            if num == 0:
                prefix_sum -= 1
            else:
                prefix_sum += 1

            # Step 3: If prefix_sum seen before
            if prefix_sum in prefix_map:
                # length of subarray = current_index - first_index
                length = i - prefix_map[prefix_sum]
                max_length = max(max_length, length)
            else:
                # store first time we see this prefix_sum
                prefix_map[prefix_sum] = i

        return max_length
