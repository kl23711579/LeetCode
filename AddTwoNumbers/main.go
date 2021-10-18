package main

import (
	"fmt"
)

// ListNode Struct
type ListNode struct {
	Val  int
	Next *ListNode
}

func main() {

	/*
	 * Input
	 * [2,4,3]
	 * [5,6,4]
	 */

	a := []int{5}
	b := []int{5}

	result := AddTwoNumbers(createNode(a), createNode(b))
	showResult(result)
}

// AddTwoNumbers FOrm
func AddTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	l1Now := l1
	l2Now := l2

	result := ListNode{
		Val:  0,
		Next: nil,
	}

	resultHead := &result
	resultNow := resultHead

	addition := 0
	for l1Now != nil || l2Now != nil {
		if l1Now == nil {
			resultNow.Val = l2Now.Val + addition
			l2Now = l2Now.Next
		} else if l2Now == nil {
			resultNow.Val = l1Now.Val + addition
			l1Now = l1Now.Next
		} else {
			resultNow.Val = l1Now.Val + l2Now.Val + addition
			l1Now = l1Now.Next
			l2Now = l2Now.Next
		}
		addition = 0
		if resultNow.Val >= 10 {
			resultNow.Val %= 10
			addition = 1
		}

		if l1Now != nil || l2Now != nil {
			NewResult := ListNode{
				Val:  0,
				Next: nil,
			}

			// point to next
			resultNow.Next = &NewResult
			resultNow = &NewResult
		}
	}

	if addition == 1 {
		NewResult := ListNode{
			Val:  addition,
			Next: nil,
		}
		resultNow.Next = &NewResult
		resultNow = &NewResult
	}

	return &result
}

func createNode(ary []int) *ListNode {
	Node := ListNode{
		Val:  0,
		Next: nil,
	}

	Head := &Node
	Now := Head

	Len := len(ary)
	for i, item := range ary {
		Now.Val = item
		if i != Len-1 {
			NewNode := ListNode{
				Val:  0,
				Next: nil,
			}
			Now.Next = &NewNode
			Now = &NewNode
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
