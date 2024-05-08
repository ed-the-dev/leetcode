from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: TreeNode = left
        self.right: TreeNode = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def get_min_value_node(root: TreeNode) -> Optional[TreeNode]:

            curr: TreeNode = root

            while curr and curr.left:
                curr = curr.left

            return curr
        
        def remove(root: TreeNode, value: int) -> TreeNode:

            if not root:
                return None
            
            if value > root.val:
                root.right = remove(root.right, value)
            elif value < root.val:
                root.left = remove(root.left, value)
            else:
                # Node found
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                else:
                    min_node: TreeNode = get_min_value_node(root.right)
                    root.val = min_node.val
                    root.right = remove(root.right, min_node.val)
            return root
        
        return remove(root, key)

