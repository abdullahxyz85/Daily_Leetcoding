class Solution:
    def canBeIncreasing(self, nums):
        def is_strictly_increasing(arr):
            for i in range(1, len(arr)):
                if arr[i - 1] >= arr[i]:  
                    return False
            return True  

        for i in range(len(nums)):  
            new_nums = []  
            for j in range(len(nums)):  
                if j != i:  
                    new_nums.append(nums[j])  
            
            if is_strictly_increasing(new_nums):  
                return True  

        return False  
