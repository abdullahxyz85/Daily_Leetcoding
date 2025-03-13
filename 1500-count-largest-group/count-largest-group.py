class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = defaultdict(int)  

        for num in range(1, n + 1):
            digit_sum = 0
            temp = num
            while temp > 0: 
                digit_sum += temp % 10
                temp //= 10
            groups[digit_sum] += 1  

        
        max_size = 0
        for size in groups.values():
            if size > max_size:
                max_size = size

    
        count = 0
        for size in groups.values():
            if size == max_size:
                count += 1

        return count