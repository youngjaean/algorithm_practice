# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moving = 0

        def dfs(node):
            if not node:
                return 0
            left_balance = dfs(node.left)
            right_balance = dfs(node.right)

            self.moving += abs(left_balance) + abs(right_balance)

            return node.val -1 + left_balance + right_balance
        dfs(root)

        return self.moving       