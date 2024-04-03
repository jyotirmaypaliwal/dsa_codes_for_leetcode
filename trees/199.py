from collections import queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
            res = []
            q = queue([root])

            while q:
                  qlen = len(q)
                  rs = None
                  for i in range(qlen):
                        node = q.popleft()
                        if node:
                              rs = node
                              q.append(node.left)
                              q.append(node.right)

                        if rs:
                              res.append(rs.val)
            
            return res