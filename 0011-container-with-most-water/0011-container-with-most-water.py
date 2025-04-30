class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # Calculate the area
            h = min(height[left], height[right])
            w = right - left
            area = h * w
            max_area = max(max_area, area)

            # Move the pointer that has the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
