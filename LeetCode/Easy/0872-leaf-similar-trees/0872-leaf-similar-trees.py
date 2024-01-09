from typing import List, Optional

def preorder(tree, root):
    left = tree.left
    right = tree.right

    nums = []
    if left is None and right is None:
        nums.append(root)
    if left is not None:
        nums.extend(preorder(left, left.val))
    if right is not None:
        nums.extend(preorder(right, right.val))
    return nums

def leaf(root: TreeNode):
    return preorder(root, root.val)

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return leaf(root1) == leaf(root2)
