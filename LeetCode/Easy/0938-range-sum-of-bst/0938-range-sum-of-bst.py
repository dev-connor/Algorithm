from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def check(node:Optional[TreeNode],low,high):
    if node == None:
        return 0
    answer = 0
    if low <= node.val <= high:
        answer += node.val
        answer += check(node.left,low,high)
        answer += check(node.right,low,high)
    elif node.val < low:
        answer += check(node.right,low,high)
    elif node.val > high:
        answer += check(node.left,low,high)
    return answer

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        answer = check(root,low,high)
        return answer