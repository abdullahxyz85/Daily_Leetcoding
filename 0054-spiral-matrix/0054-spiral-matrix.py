class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom and left <= right:

            # 1. Go RIGHT
            for i in range(left, right + 1):
                result.append(matrix[top][i])

            top = top + 1

            # 2. Go DOWN
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])

            right = right - 1

            # 3. Go LEFT
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])

                bottom = bottom - 1

            # 4. Go UP
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])

                left = left + 1

        return result