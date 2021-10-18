package main

import "fmt"

func main(){
	nums := []int{2}
	fmt.Println(removeElement(nums, 2))
	fmt.Println(nums)
}

func removeElement(nums []int, val int) int {
	aLength := len(nums)
	index := 0

	if aLength == 0 {
		return 0
	}

	for i := 0; i < aLength; i++ {
		if nums[index] == val {
			deleteElement(nums, index)
			index--
		}
		index++
	}

	nums = nums[:index]
	return len(nums)
}

func deleteElement(nums []int, index int) {
	length := len(nums)
	for i := index; i < length-1 ; i++ {
		j := nums[i]
		nums[i] = nums[i+1]
		nums[i+1] = j
	}
}
