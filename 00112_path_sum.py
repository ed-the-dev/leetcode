from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: TreeNode = left
        self.right: TreeNode = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:


        def dfs(node: TreeNode, current_sum: int) -> bool:
            if not node:
                return False 

            current_sum += node.val

            if current_sum == targetSum and not node.left and not node.right:
                return True
            
            return dfs(node.left, current_sum) or dfs(node.right, current_sum)

        return dfs(root, 0)
            

    