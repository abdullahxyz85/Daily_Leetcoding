class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        results = set()

        for a, b, c in permutations(digits, 3):
            if a == 0:
                continue
            if c % 2 != 0:
                continue
            num = a * 100 + b * 10 + c
            results.add(num)

        return len(results)