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

def prettyPrintTree(node, prefix="", isLeft=True):
    if not node:
        print("Empty Tree")
        return

    if node.right:
        prettyPrintTree(node.right, prefix + ("│   " if isLeft else "    "), False)

    print(prefix + ("└── " if isLeft else "┌── ") + str(node.val))

    if node.left:
        prettyPrintTree(node.left, prefix + ("    " if isLeft else "│   "), True)


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


node = listToTreeNode([1,2,None,3,4,5,6,None,7])
prettyPrintTree(node)
print(treeNodeToString(node))