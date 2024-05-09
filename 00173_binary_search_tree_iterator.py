from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: TreeNode = left
        self.right: TreeNode = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):

        self.stack: list[TreeNode] = []
        self.current: TreeNode = root
        

    def next(self) -> int:

        while True:
                
            if self.current:
                self.stack.append(self.current)
                self.current = self.current.left

            else:
                self.current = self.stack.pop()
                value: int = self.current.val
                self.current = self.current.right
                return value
        

    def hasNext(self) -> bool:

        if self.stack or self.current:
            return True
        return False

        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()