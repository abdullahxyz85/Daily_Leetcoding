class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        s = set()
        sol = []

        for i in nums:
            if i in s:
                sol.append(i)
            else:
                s.add(i)
        return sol
