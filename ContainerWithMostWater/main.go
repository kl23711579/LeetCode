package main

import "fmt"

func main() {
	h := []int{1,8,6,2,5,4,8,3,7}
	fmt.Println(maxArea(h))
}

func maxArea(height []int) int {
	area := 0

	for i, j := 0, len(height)-1; i <= j; {
		long := min(height[i], height[j])
		area = max(long * (j - i), area)

		if height[i] >= height[j] {
			j--
		} else {
			i++
		}
	}
	return area
}

func max(x,y int) int {
	if x > y {
		return x
	}
	return y
}

func min(x,y int) int {
	if x > y {
		return y
	}
	return x
}