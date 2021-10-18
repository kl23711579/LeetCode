package main

import "fmt"

func main() {

	aNum := []int{1,2,2,2,2,2,2,2,2,2,2}

	fmt.Println(removeDuplicates(aNum))

}

func removeDuplicates(num []int) int {
	index := 1
	count := 0
	aLength := len(num)

	if aLength == 0 {
		return 0
	}

	for i := 0; i < aLength; i++{
		// over the length of array, finish loop
		if index >= aLength || count >= aLength{
			break
		}
		if num[index-1] == num[index]{
			deleteElement(num, index)
			index--
		} else if num[index-1] > num[index] {
			break
		}
		index++
	}

	num = num[:index]

	return len(num)
}

func deleteElement(ary []int, index int) {
	for i := index-1; i < len(ary)-1; i++ {
		j := ary[i]
		ary[i] = ary[i+1]
		ary[i+1] = j
	}
}

