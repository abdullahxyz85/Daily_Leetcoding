class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        int_count = {}
        for count in arr:
            if count in int_count:
                int_count[count] += 1
            else:
                int_count[count] = 1
        occurences = list(int_count.values())
        for i in range(len(occurences)):
            for j in range(i + 1, len(occurences)):
                if occurences[i] == occurences[j]:
                    return False
        return True