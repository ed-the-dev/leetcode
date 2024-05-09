from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: TreeNode = left
        self.right: TreeNode = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        count: int = 1

        current: TreeNode = root
        stack: list[TreeNode] = []

        while current or stack:

            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                if count == k:
                    return current.val
                count += 1
                current = current.right
    
solution: Solution = Solution()
print(solution.kthSmallest(TreeNode(1), 1))