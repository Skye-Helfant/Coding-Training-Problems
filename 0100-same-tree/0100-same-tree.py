# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both trees are empty, return True
        if not p and not q:
            return True
        
        # If one of the trees is empty, return False
        if not p or not q:
            return False
        
        # If the value of their root node is not the same, return False
        if p.val != q.val:
            return False
        
        # Recur for their left subtree and right subtree
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
