from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: TreeNode = left
        self.right: TreeNode = right

class Solution:

    # 'Trivial' recursive solution.

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        result: list[int] = []

        def inorder_traverse(root: TreeNode) -> None:

            result.append(root.val)

            if root.left:
                inorder_traverse(root.left)
            if root.right:
                inorder_traverse(root.right)
            return
        
        if root:
            inorder_traverse(root)

        return result
        