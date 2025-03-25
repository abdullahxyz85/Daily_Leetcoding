class Solution:
    def minimumSum(self, num: int) -> int:
        d1 = num // 1000       # First digit
        d2 = (num // 100) % 10  # Second digit
        d3 = (num // 10) % 10   # Third digit
        d4 = num % 10           # Fourth digit

        # Step 2: Store digits in an array and sort them
        digits = [d1, d2, d3, d4]
        
        # Manual sorting (without using sort method)
        for i in range(4):
            for j in range(i + 1, 4):
                if digits[i] > digits[j]:
                    digits[i], digits[j] = digits[j], digits[i]

        # Step 3: Form two numbers
        new1 = digits[0] * 10 + digits[2]  # Smallest + 3rd smallest
        new2 = digits[1] * 10 + digits[3]  # 2nd smallest + Largest

        # Step 4: Return the sum
        return new1 + new2
