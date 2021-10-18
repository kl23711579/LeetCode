package main

import "fmt"

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
type TreeNode struct {
	Val int
	Left *TreeNode
	Right *TreeNode
	Parent *TreeNode
}

func main() {
	list := []int{1,2,2,3,4,4,3}
	tree := getTree(list)
	showTree(tree)
	fmt.Println(isSymmetric(tree))
}

func getTree(list []int) *TreeNode {
	root := TreeNode{list[0], nil, nil, nil}

	insertIntoTree(list, 0, &root)

	return &root
}

func insertIntoTree(list []int, index int, head *TreeNode) {
	if index*2+1 >= len(list) {
		return
	}

	leftNode := TreeNode{list[index*2+1], nil ,nil ,nil}
	head.Left = &leftNode
	leftNode.Parent = head
	insertIntoTree(list, index*2+1, head.Left)

	if index*2+2 >= len(list) {
		return
	}

	rightNode := TreeNode{list[index*2+2], nil, nil, nil}
	head.Right = &rightNode
	rightNode.Parent = head
	insertIntoTree(list, index*2+2, head.Right)

}

func showTree(head *TreeNode) {
	fmt.Println(head.Val)
	if head.Left != nil {
		showTree(head.Left)
	}
	if head.Right != nil {
		showTree(head.Right)
	}
}

func isSymmetric(root *TreeNode) bool {
	if root == nil {
		return true
	}
	return compare(root.Left, root.Right)
}

func compare(left, right *TreeNode) bool {
	if left == nil && right == nil { // all nil
		return true
	} else if left == nil || right == nil { // just one nil
		return false
	}

	if left.Val != right.Val {
		return false
	} else {
		if !compare(left.Left, right.Right) {
			return false
		} else if !compare(left.Right, right.Left) {
			return false
		}
	}
	return true
}