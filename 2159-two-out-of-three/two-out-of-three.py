class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        # Step 1: Convert lists to sets to remove duplicate values within each list
        set1 = set(nums1)
        set2 = set(nums2)
        set3 = set(nums3)
        
        # Step 2: Create a dictionary to keep track of occurrences in different sets
        count = {}  # This will store the frequency of each number across sets

        # Step 3: Count occurrences of numbers in the first set
        for num in set1:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        # Step 4: Count occurrences of numbers in the second set
        for num in set2:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        # Step 5: Count occurrences of numbers in the third set
        for num in set3:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        # Step 6: Extract numbers that appear in at least two sets
        result = []
        for num, freq in count.items():
            if freq >= 2:  # If a number is present in at least two sets
                result.append(num)

        # Step 7: Return the result
        return result

