class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        count = 0  # This will store the total number of good pairs

        for i in range(len(nums1)):           # Loop through nums1
            for j in range(len(nums2)):       # Loop through nums2
                if nums1[i] % (nums2[j] * k) == 0:
                    count += 1  # It's a good pair, so increase the count

        return count
