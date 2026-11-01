class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        new_arr = []
        for i in range(n):
            if arr[i] == 0:
                new_arr.append(0)
                new_arr.append(0)
            else:
                new_arr.append(arr[i])
        # don't want to return and modify so we assign new arr to older arr
        for i in range(n):
            arr[i] = new_arr[i]