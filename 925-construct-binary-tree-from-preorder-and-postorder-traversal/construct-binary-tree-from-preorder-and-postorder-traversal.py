# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder:
            return None

        root = TreeNode(preorder[0])  # The first element in preorder is the root
        if len(preorder) == 1:
            return root  # Base case: single node tree

        left_subroot_val = preorder[1]  # Second element is the root of the left subtree
        left_subroot_idx = postorder.index(left_subroot_val)  # Find the left subtree boundary

        # Recursively construct the left and right subtrees
        root.left = self.constructFromPrePost(preorder[1:left_subroot_idx+2], postorder[:left_subroot_idx+1])
        root.right = self.constructFromPrePost(preorder[left_subroot_idx+2:], postorder[left_subroot_idx+1:-1])

        return root