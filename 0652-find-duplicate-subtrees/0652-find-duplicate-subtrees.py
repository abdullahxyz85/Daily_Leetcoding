# Definition for a binary tree node.
# class TreeNode:
#     def _init_(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        count = defaultdict(int)
        result = []
        def serialize(node):
            if not node:
                return None
            left_serial = serialize(node.left)
            right_serial = serialize(node.right)
            serial = f"{node.val},{left_serial},{right_serial}"
            count[serial] +=1

            if count[serial] ==2:
                result.append(node)
            return serial

        serialize (root)
        return result