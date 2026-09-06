# Last updated: 9/6/2026, 2:56:15 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # When the node has no child nodes, recursively calling
        # self.invertTree(arg) would yield None so simply return None
        if root is None:
            return None
        # The root has left and right children nodes
        else:
            # Swap the nodes and values without temp variables
            root.left, root.right = root.right, root.left

            # Recursively call for each child node
            self.invertTree(root.left)
            self.invertTree(root.right)

            # Return the root array
            return root
