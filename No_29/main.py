from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        
        root = TreeNode(preorder[0])

        pivot = inorder.index(preorder[0]) # every element below or equal left_index is in left sub tree

        if len(preorder) == 1:
            return root

        root.left = self.buildTree(preorder[1:pivot+1], inorder[:pivot])
        root.right = self.buildTree(preorder[pivot+1:], inorder[pivot+1:])

        return root

if __name__ == "__main__":
    s = Solution()
    preorder = [3,9,8,10,5,2,20,15,7]
    inorder = [10,8,5,9,2,3,15,20,7]
    t = s.buildTree(preorder, inorder)
    print(treeNodeToString(t))

    preorder = [3,9,8,10,5,20,15,7]
    inorder = [10,8,5,9,3,15,20,7]
    t = s.buildTree(preorder, inorder)
    print(treeNodeToString(t))

