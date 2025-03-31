class Solution:
    def minElement(self, nums: List[int]) -> int:
        answer = []
        for num in nums:
            sum_digits = 0
            while num > 0:
                sum_digits += num % 10
                num //= 10
            answer.append(sum_digits)
        return min(answer)