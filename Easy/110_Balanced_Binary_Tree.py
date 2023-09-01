# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root):
        def check_balance(node):
            if not node:
                return 0

            left_depth = check_balance(node.left)
            if left_depth == -1:
                return -1

            right_depth = check_balance(node.right)
            if right_depth == -1:
                return -1

            if abs(left_depth - right_depth) > 1:
                return -1

            return 1 + max(left_depth, right_depth)

        return check_balance(root) != -1


# Includes TestCases
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# tree = [1, 2, 2, 3, None, None, 3, 4, None, None, None, None, None, None, 4]
# tree2 = [1, 2, 2, 3, 3, None, None, 4, 4]
# tree3 = [2, 1, 4, None, None, 3, 5, None, None, None, None, None, None, 6]


# def build_subtree(tree_list, idx=0):
#     root = TreeNode()
#     if tree_list[idx] == None:
#         return None
#     root.val = tree_list[idx]
#     if 2*idx+1 <= len(tree_list)-1:
#         root.left = build_subtree(tree_list, idx=2*idx+1)
#     if 2*(idx + 1) <= len(tree_list)-1:
#         root.right = build_subtree(tree_list, idx=2*(idx+1))
#     return root


# root = build_subtree(tree3)

# sol = Solution()
# answer = sol.isBalanced(root)
# print(answer)
