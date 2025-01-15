class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        int_count = {}
        for count in arr:
            if count in int_count:
                int_count[count] += 1
            else:
                int_count[count] = 1
        occurrences = list(int_count.values())
        for i in range(len(occurrences)):
            for j in range(i + 1, len(occurrences)):
                if occurrences[i] == occurrences[j]:
                    return False
        return True
