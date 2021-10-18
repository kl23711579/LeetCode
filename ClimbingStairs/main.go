package main

import "fmt"

func main() {
	fmt.Println(climbStairs(30))
}

func climbStairs(n int) int {
	if n == 0 {
		return 0
	} else if n == 1 {
		return 1
	} else if n == 2 {
		return 2
	}

	fordwarTwoSteps := 1
	fordwarOneSteps := 2
	totalSteps := 0

	for i := 3; i <= n; i++ {
		totalSteps = fordwarOneSteps + fordwarTwoSteps
		fordwarTwoSteps = fordwarOneSteps
		fordwarOneSteps = totalSteps
	}

	return totalSteps
}

// Because using recursing will TLE

//func climbStairs(n int) int {
//	if n == 0 {
//		return 0
//	} else if n == 1 {
//		return 1
//	} else if n == 2 {
//		return 2
//	}
//
//	return climbStairs(n-1) + climbStairs(n-2)
//}