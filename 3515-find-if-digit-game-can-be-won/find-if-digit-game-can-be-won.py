class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single_sum = 0
        double_sum = 0
        for i in nums:
            i = str(i)
            if len(i) == 2:
                double_sum += int(i)
            else:
                single_sum += int(i)
        if single_sum>double_sum or double_sum > single_sum:
            return True
        return False

    #     class Solution:
    # def canAliceWin(self, nums: List[int]) -> bool:
    #     single_sum = 0
    #     double_sum = 0
        
    #     for num in nums:
    #         if num < 10:  
    #             single_sum += num
    #         else:  
    #             double_sum += num
        
    #     return single_sum > double_sum or double_sum > single_sum