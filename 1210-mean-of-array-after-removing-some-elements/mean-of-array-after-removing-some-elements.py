class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort() 
        n = len(arr)
        remove_count = n // 20  

        trimmed_arr = arr[remove_count:-remove_count] 
        mean_value = sum(trimmed_arr) / len(trimmed_arr) 

        return round(mean_value, 5)  