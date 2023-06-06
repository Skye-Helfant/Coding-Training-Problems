# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                print("Reached a leaf node. Returning [True, 0]")
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0] and 
                        abs(left[1] - right[1]) <= 1)
            print("Checking if node with value", root.val, "is balanced. Left subtree height:", left[1], "Right subtree height:", right[1], "Balanced:", balanced)

            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]

