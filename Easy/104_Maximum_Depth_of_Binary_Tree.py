class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #DFS
        if root is None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1
