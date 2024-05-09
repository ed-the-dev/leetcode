from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: TreeNode = left
        self.right: TreeNode = right

class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        #  Neetcode has much less verbose code.
        def build_level(pre_order: list[int], in_order: list[int]):

            root: TreeNode = TreeNode(pre_order[0])

            # Find index of root in Inorder

            root_index: int = in_order.index(pre_order[0])

            lhs_inorder: list[int] = in_order[:root_index]

            rhs_inorder: list[int] = in_order[root_index+1:]

            if lhs_inorder:
                # make preorder array for lhs
                lhs_pre_order: list[int] = pre_order[1:len(lhs_inorder)+1]
                root.left = build_level(lhs_pre_order, lhs_inorder)
            else: 
                root.left = None

            if rhs_inorder:
                rhs_pre_order: list[int] = pre_order[len(lhs_inorder)+1:]
                root.right = build_level(rhs_pre_order, rhs_inorder)
            else:
                root.right = None

            return root

        build_level(preorder, inorder)


solution: Solution = Solution()
solution.buildTree([3,9,20,15,7], [9,3,15,20,7])