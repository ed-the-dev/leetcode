from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if root.val == val:
            return root
        
        elif root.right and val > root.val:
            return self.searchBST(root.right, val)
        elif root.left and val < root.val:
            return self.searchBST(root.left, val)
        else:
            return None
        

node_1: TreeNode = TreeNode(val=1)
node_3: TreeNode = TreeNode(val=3)
node_2: TreeNode = TreeNode(val=2, left=node_1, right=node_3)
node_7: TreeNode = TreeNode(val=7)
node_4: TreeNode = TreeNode(val=4, left=node_2, right=node_7)

solution: Solution = Solution()

result = solution.searchBST(node_4, 2)

print(result.val)