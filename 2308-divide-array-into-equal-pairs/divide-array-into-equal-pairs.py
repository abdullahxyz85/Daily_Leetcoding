class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = {}  
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        for value in freq.values():
            if value % 2 != 0:  
                return False

        return True  

        # nums.sort() 
        # for i in range(0, len(nums), 2):  
        #     if nums[i] != nums[i + 1]: 
        #         return False
        # return True  
