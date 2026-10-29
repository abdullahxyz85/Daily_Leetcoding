
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False

        sum = root.val

        if root.left is None and root.right is None:
            return targetSum == sum

        if self.hasPathSum(root.left, targetSum - sum):
            return True

        if self.hasPathSum(root.right, targetSum - sum):
            return True

        return False
