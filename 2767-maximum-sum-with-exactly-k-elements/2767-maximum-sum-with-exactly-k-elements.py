class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        score = 0
        current_max = max(nums) 

        for i in range(k):      
            score += current_max
            current_max += 1    

        return score
