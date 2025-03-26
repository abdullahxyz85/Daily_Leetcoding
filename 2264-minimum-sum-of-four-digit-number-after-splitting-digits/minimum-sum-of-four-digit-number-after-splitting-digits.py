class Solution:
    def minimumSum(self, num: int) -> int:
        # d1 = num // 1000      #2932 // 1000 = 2                                                   # Input: num = 2932
        #                                                                         #  Output: 52   
        # d2 = (num // 100) % 10   #2932 // 100 = 29 % 10 = 9
        # d3 = (num // 10) % 10   #2932 // 10 = 293 % 10 = 3
        # d4 = num % 10           #2932 % 10 = 2

        # digits = [d1, d2, d3, d4] #[2, 9, 3, 2]

        digits = []
        str_num = str(num)
        for i in str_num:
            digits.append(int(i))


        digits.sort()
        
        # for i in range(4):
        #     for j in range(i + 1, 4):
        #         if digits[i] > digits[j]: 
        #             digits[i], digits[j] = digits[j], digits[i]  # [2, 2, 3, 9] # [0, 1, 2, 3]
        
        new1 = digits[0] * 10 + digits[2]  #2 * 10 + 3 = 23
        new2 = digits[1] * 10 + digits[3]  #2 * 10 + 9 = 29

        return new1 + new2
