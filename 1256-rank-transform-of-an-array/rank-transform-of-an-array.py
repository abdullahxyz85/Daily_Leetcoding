class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_unique = sorted(set(arr))
        
        # Step 2: Create a dictionary to store ranks
        rank_map = {}
        rank = 1
        for num in sorted_unique:
            rank_map[num] = rank
            rank += 1

        # Step 3: Replace elements with their ranks
        result = []
        for num in arr:
            result.append(rank_map[num])

        return result