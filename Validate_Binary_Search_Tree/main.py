# Defination for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(self, root):
    def helper(node, min_val, max_val):
        if not node: return True
        if node.val >= max_val or node.val <= min_val: return False
        # go left node
        if not helper(node.left, min_val, node.val): return False
        # go right node
        if not helper(node.right, node.val, max_val): return False
        return True
    return  helper(root, float(-inf), float(inf))
