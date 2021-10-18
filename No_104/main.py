class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def listToTreeNode(input: list[int]):
    root = TreeNode(input[0])
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(input):
        # the node which is going to append child
        node = nodeQueue[front]
        front = front + 1
        
        # items which are going to be appended
        item = input[index]
        index = index + 1

        if item:
            node.left = TreeNode(item)
            nodeQueue.append(node.left)

        # check index
        if index >= len(input):
            break

        item = input[index]
        index = index + 1

        if item:
            node.right = TreeNode(item)
            nodeQueue.append(node.right)

    return root

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

s = Solution()
t1 = listToTreeNode([3,9,20,None,None,15,7])
print(s.maxDepth(t1))