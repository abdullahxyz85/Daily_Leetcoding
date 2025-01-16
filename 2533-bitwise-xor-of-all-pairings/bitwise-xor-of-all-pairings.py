class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # XOR of all elements in nums1
        xor1 = 0
        for num in nums1:
            xor1 ^= num

        # XOR of all elements in nums2
        xor2 = 0
        for num in nums2:
            xor2 ^= num

        # Calculate the final result
        result = 0
        if len(nums2) % 2 != 0:  # If nums2 has odd length, xor1 contributes
            result ^= xor1
        if len(nums1) % 2 != 0:  # If nums1 has odd length, xor2 contributes
            result ^= xor2
        
        return result

