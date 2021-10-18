package main

import "fmt"

// structure ListNode
type ListNode struct {
	Val int
	Next *ListNode
}

func main() {

	/*
	 * Input
	 * [2,4,3]
	 * [5,6,4]
	 */

	a := []int{}
	b := []int{}

	result := mergeTwoLists(createNode(a), createNode(b))
	showResult(result)
}

// function mergeTwoLists
func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode{
	l1Now := l1
	l2Now := l2

	if l1Now == nil && l2Now == nil {
		return nil
	}

	result := ListNode {
		Val: 0,
		Next: nil,
	}

	resultHead := &result
	resultNow := resultHead

	for l1Now != nil || l2Now != nil {
		if l1Now == nil {
			resultNow.Val = l2Now.Val
			l2Now = l2Now.Next
		} else if l2Now == nil {
			resultNow.Val = l1Now.Val
			l1Now = l1Now.Next
		} else {
			if l1Now.Val <= l2Now.Val {
				resultNow.Val = l1Now.Val
				l1Now = l1Now.Next
			} else if l1Now.Val > l2Now.Val {
				resultNow.Val = l2Now.Val
				l2Now = l2Now.Next
			}
		}

		if l1Now != nil || l2Now != nil {
			newNode := ListNode {
				Val: 0,
				Next: nil,
			}

			// point to next
			resultNow.Next = &newNode
			resultNow = resultNow.Next
		}
	}

	return resultHead

}

func createNode(ary []int) *ListNode {
	Node := ListNode{
		Val: 0,
		Next: nil,
	}

	Head := &Node
	Now := Head

	Len := len(ary)
	for i, item := range ary {
		Now.Val = item
		if i != Len-1 {
			NewNode := ListNode {
				Val: 0,
				Next: nil,
			}
			Now.Next = &NewNode
			Now = Now.Next
		}
	}

	return Head
}

func showResult(list *ListNode) {
	Now := list
	for Now != nil {
		fmt.Printf("%d - ", Now.Val)
		Now = Now.Next
	}
}
