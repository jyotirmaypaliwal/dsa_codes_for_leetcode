# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        count = k
        def inord(root):
            if not root:
                return 
            inord(root.left)
            res.append(root.val)
            inord(root.right)

        inord(root)
        return res[k-1]
