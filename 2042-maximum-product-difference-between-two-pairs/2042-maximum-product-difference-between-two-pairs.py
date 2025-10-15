class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # first need to choose indices.
        # nums = [5]
        # result = []  # [7, 6, 2, 4]
        # max_num1 = max(nums)
        # nums.remove(max_num1)
        # result.append(max_num1)
        # max_num2 = max(nums)
        # nums.remove(max_num2)
        # result.append(max_num2)
        # min_num1 = min(nums)
        # nums.remove(min_num1)
        # result.append(min_num1)
        # min_num2 = min(nums)
        # nums.remove(min_num2)
        # result.append(min_num2)

        # return (result[0] * result[1]) - (result[2] * result[3])

        nums_sorted = sorted(nums)
        
        return (nums_sorted[-1] * nums_sorted[-2]) - (nums_sorted[0] * nums_sorted[1])
