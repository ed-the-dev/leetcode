from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: TreeNode = left
        self.right: TreeNode = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        stack: list[tuple[TreeNode, bool]] = [(root, False)]

        result: list[int] = []

        while stack:

            current: tuple[TreeNode, bool] = stack.pop()

            if current[0]:
                
                if not current[1]:
                    stack.append((current[0], True))
                    stack.append((current[0].right, False))
                    stack.append((current[0].left, False))
                else:
                    result.append(current[0].val)
        
        return result

