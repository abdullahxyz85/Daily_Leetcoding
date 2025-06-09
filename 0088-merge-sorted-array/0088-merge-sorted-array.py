from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Step 1: Extract the first `m` elements from nums1 into a new list
        new_nums1 = []
        for i in range(m):
            new_nums1.append(nums1[i])  # Append elements manually
        
        # Step 2: Merge new_nums1 and nums2
        merged = new_nums1 + nums2  # Concatenate the lists
        
        # Step 3: Sort the merged list
        merged.sort()  # Sort in ascending order
        
        # Step 4: Copy the sorted elements back to nums1
        for i in range(len(merged)):
            nums1[i] = merged[i]  # Modify nums1 in-place
