from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: TreeNode = left
        self.right: TreeNode = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        stack: list[TreeNode] = []
        current: TreeNode = root

        result: list[int] = [] 

        while current or stack:
            if current:
                result.append(current.val)
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                current = current.right