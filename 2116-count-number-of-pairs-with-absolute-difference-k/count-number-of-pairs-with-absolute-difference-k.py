class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        for  i in range(len(nums)):
            for  j in range(i + 1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    count += 1
        return count

#  Second Approach:
# class Solution:
#     def countKDifference(self, nums: List[int], k: int) -> int:
#         freq = defaultdict(int)  # Dictionary to store frequency of numbers
#         count = 0
        
#         for num in nums:
#             count += freq[num - k]  # Check if (num - k) exists in hashmap
#             count += freq[num + k]  # Check if (num + k) exists in hashmap
#             freq[num] += 1  # Store the count of the current number
        
#         return count