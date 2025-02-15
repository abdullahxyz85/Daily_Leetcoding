class Solution:
    def canPartition(self, num_str: str, target: int, index: int = 0, current_sum: int = 0) -> bool:
        """Helper function to check if num_str can be partitioned into contiguous substrings summing to target."""
        if index == len(num_str):  
            return current_sum == target  # Check if the sum matches target

        for j in range(index, len(num_str)):
            part = int(num_str[index:j+1])  # Convert substring to integer
            if current_sum + part > target:
                break  # No need to continue if sum exceeds target
            if self.canPartition(num_str, target, j + 1, current_sum + part):
                return True
        return False

    def punishmentNumber(self, n: int) -> int:
        """Calculates the punishment number of n."""
        total_sum = 0

        for i in range(1, n + 1):
            square_str = str(i * i)  
            if self.canPartition(square_str, i):  # Check if i*i can be partitioned to sum to i
                total_sum += i * i  # Add to punishment number

        return total_sum
