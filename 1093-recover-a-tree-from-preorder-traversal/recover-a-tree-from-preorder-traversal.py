
class Solution(object):
    def recoverFromPreorder(self, S):
        """
        :type S: str
        :rtype: TreeNode
        """
        i = 0
        stack = []
        while i < len(S):
            level = 0
            while i < len(S) and S[i] == '-':  # Counting dashes
                level += 1
                i += 1
            while len(stack) > level:  # Pop stack to maintain correct depth
                stack.pop()
            val = []
            while i < len(S) and S[i] != '-':  # Extract node value
                val.append(S[i])
                i += 1
            node = TreeNode(int("".join(val)))
            if stack:
                if stack[-1].left is None:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
            stack.append(node)
        return stack[0]  # Return root node of the tree

