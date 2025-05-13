class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        # result = [0] * len(nums) 
        # even_index = 0  
        # odd_index = 1   

        # for num in nums:
        #     if num % 2 == 0:
        #         result[even_index] = num
        #         even_index += 2
        #     else:
        #         result[odd_index] = num
        #         odd_index += 2

        # return result

        ans = []
        even = []
        odd = []

        for num in nums:
            if num % 2 == 0:
                even.append(num)
            elif num % 2 != 0:
                odd.append(num)
                
        for i in range(len(even)):  
            ans.append(even[i])
            ans.append(odd[i])
            
        return ans
            