class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target_count = Counter(target)
        arr_count = Counter(arr)

        if target_count == arr_count:
            return True
        else:
            return False
