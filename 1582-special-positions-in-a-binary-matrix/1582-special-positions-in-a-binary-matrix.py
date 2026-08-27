class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m = len(mat)
        n = len(mat[0])

        count = 0

        for i in range(m):
            for j in range(n):

                if mat[i][j] == 1:

                    row_count = 0
                    for col in range(n):
                        if mat[i][col] == 1:
                            row_count += 1

                    col_count = 0
                    for row in range(m):
                        if mat[row][j] == 1:
                            col_count += 1

                    if row_count == 1 and col_count == 1:
                        count += 1

        return count
        