class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = None
        
        for num in nums:
            if num in (first, second, third):
                continue  # Skip duplicates
            
            if first is None or num > first:
                third, second, first = second, first, num
            elif second is None or num > second:
                third, second = second, num
            elif third is None or num > third:
                third = num

        return third if third is not None else first