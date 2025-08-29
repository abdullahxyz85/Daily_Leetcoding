class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        lucky_numbers = []
        for num, count in freq.items():
            if num == count:  
                lucky_numbers.append(num)

        if not lucky_numbers:  
            return -1
        else:
            return max(lucky_numbers) 