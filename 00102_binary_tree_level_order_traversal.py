from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: TreeNode = left
        self.right: TreeNode = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue: deque = deque()

        if root:
            queue.append(root)

        levels: list[list[int]] = []
        level = 0

        while len(queue) > 0:

            level: list[int] = []

            for index in range(len(queue)):
                current: TreeNode = queue.popleft()
                level.append(current.val)

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            
            levels.append(level)
        
        return levels