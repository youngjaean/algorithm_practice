# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        que = [root]
        answer = []
        while que:
            val = que.pop()
            answer.append(val.val)
            if val.left:
                que.append(val.left)
            if val.right:
                que.append(val.right)

        return answer[::-1]