# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class TreeList:
#     def __init__(self, nodes: list[int]):
#         if len(nodes) > 0:
#             self.head = nodes[0]

#     def addNode

class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        res, level = [], [root]
        while root and level:
            res.append([node.val for node in level])
            pairs = [(node.left, node.right) for node in level]
            level = [ node for nodes in pairs for node in nodes if node ]
            
        return res;