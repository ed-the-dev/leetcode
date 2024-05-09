from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: TreeNode = left
        self.right: TreeNode = right

class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        stack: list[TreeNode] = []
        curr: TreeNode = root
        result: list[int] = []

        while curr or stack:

            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                result.append(curr.val)
                curr = curr.right
        
        return result


    # 'Trivial' recursive solution.

    def inorderTraversalRecursive(self, root: Optional[TreeNode]) -> List[int]:

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
        