class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            square = i * i
            res.append(square)
        
        return sorted(res)  # Correct sorting method

