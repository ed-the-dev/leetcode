from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: TreeNode = left
        self.right: TreeNode = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        queue: deque = deque()

        if root:
            queue.append(root)

        right_side: list[int] = []

        while len(queue) > 0:

            for index in range(len(queue)):

                current: TreeNode = queue.popleft()
                if index == 0:
                    right_side.append(current.val)
                if current.right:
                    queue.append(current.right)
                if current.left:
                    queue.append(current.left)
                
        return right_side