class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        value1 = abs(x - z)
        value2 = abs(y - z)
        if value1 < value2:
            return 1
        elif value2 < value1:
            return 2
        else:
            return 0