class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        seen_sums = set()  
        for i in range(len(nums) - 1):        
            current_sum = nums[i] + nums[i + 1]

            if current_sum in seen_sums:
                return True  

            seen_sums.add(current_sum)

        return False

    #[4, 2, 4]

    #i = 1
    
    # nums[1] + nums[1 + 1] 2 + 4 = 6