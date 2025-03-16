class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        left, right = 1, min(ranks) * (cars ** 2)  # Binary search range
        
        def canRepairInTime(T):
            total_cars = 0
            for r in ranks:
                total_cars += int(sqrt(T / r))  # Cars repaired by this mechanic
                if total_cars >= cars:  # No need to check further
                    return True
            return False

        while left < right:
            mid = (left + right) // 2
            if canRepairInTime(mid):
                right = mid  # Try a smaller time
            else:
                left = mid + 1  # Increase time
        
        return left
