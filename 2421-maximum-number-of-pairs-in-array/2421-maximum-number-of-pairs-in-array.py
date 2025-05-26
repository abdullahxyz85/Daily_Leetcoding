class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        used = []   
        pairs = 0   

        for num in nums:
            if num in used:
                pairs += 1
                used.remove(num)
            else:
                used.append(num)

        leftovers = len(used)

        return [pairs, leftovers]
