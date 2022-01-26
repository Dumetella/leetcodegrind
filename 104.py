/*
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example:

Input: root = [3,9,20,null,null,15,7]
Output: 3

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100

*/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #recursive DFS
    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        if root:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        else:
            return 0
    #BFS
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            depth = 0
            q = [root]
            while len(q) != 0:
                depth += 1
                for i in range(0, len(q)):
                    if q[0].left:
                        q.append(q[0].left)
                    if q[0].right:
                        q.append(q[0].right)
                    del q[0]
        else:
            return 0
        return depth
