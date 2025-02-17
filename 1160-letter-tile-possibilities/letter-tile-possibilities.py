class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # This will hold the count of distinct sequences
        result = set()

        # Helper function for backtracking
        def backtrack(path, tiles_left):
            if path:
                result.add(path)  # Add non-empty paths to result
            for i in range(len(tiles_left)):
                # Skip duplicate tiles to avoid counting the same sequence
                if i > 0 and tiles_left[i] == tiles_left[i - 1]:
                    continue
                backtrack(path + tiles_left[i], tiles_left[:i] + tiles_left[i + 1:])

        # Sort the tiles to handle duplicates in an orderly manner
        backtrack("", sorted(tiles))
        return len(result)
