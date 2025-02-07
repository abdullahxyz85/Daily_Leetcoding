class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_colors = {}  # Stores ball to color mapping
        distinct_colors = set()  # Stores unique colors
        color_count = {}  # Tracks occurrences of each color
        result = []

        for ball, color in queries:
            if ball in ball_colors:  # If ball already has a color
                prev_color = ball_colors[ball]
                color_count[prev_color] -= 1  # Reduce previous color count
                if color_count[prev_color] == 0:
                    distinct_colors.remove(prev_color)  # Remove color if it's gone

            # Assign new color
            ball_colors[ball] = color
            if color not in color_count:
                color_count[color] = 0
            color_count[color] += 1
            distinct_colors.add(color)  # Ensure the color is counted

            # Append the current count of distinct colors
            result.append(len(distinct_colors))

        return result
