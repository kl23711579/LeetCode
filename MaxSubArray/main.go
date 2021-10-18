package main

import (
	"fmt"
	"math"
)

func main() {
	num := []int{2,0,-3,2,1,0,1,-2}
	fmt.Println(maxSubArray(num))
	fmt.Println(maxSubArrayDivide(num, 0, len(num)-1))
}

func maxSubArray(num []int) int {
	if len(num) == 0 {
		return 0
	} else if len(num) == 1 {
		return num[0]
	}

	globalMax := num[0]
	localMax := num[0]

	for i := 1; i < len(num); i++ {
		localMax = Max(num[i], localMax+num[i])
		globalMax = Max(globalMax, localMax)
	}

	return globalMax
}

func maxSubArrayDivide(num []int, low int, high int) (int, int, int) {
	if low == high {
		return low, high, num[low]
	} else {
		var middle int
		middle = (low+high)/2
		leftLow, leftHigh, leftSum := maxSubArrayDivide(num, low, middle)
		rightLow, rightHigh, rightSum := maxSubArrayDivide(num, middle+1, high)
		crossLow, crossHigh, crossSum := findCrossingMax(num, low, middle, high)

		if leftSum >= rightSum && leftSum >= crossSum {
			return leftLow, leftHigh, leftSum
		} else if rightSum >= leftSum && rightSum >= crossSum {
			return rightLow, rightHigh, rightSum
		} else {
			return crossLow, crossHigh, crossSum
		}
	}
}

func findCrossingMax(num []int, low int, mid int, high int) (int, int, int) {
	//Firstly for middle to left
	sum := 0
	leftSum := math.MinInt32
	leftMax := mid
	for i := mid; i >= low; i-- {
		sum += num[i]
		if sum >= leftSum {
			leftSum = sum
			leftMax = i
		}
	}
	sum = 0
	rightSum := math.MinInt32
	rightMax := mid
	for i := mid+1; i < len(num); i++ {
		sum += num[i]
		if sum >= rightSum {
			rightSum = sum
			rightMax = i
		}
	}

	return leftMax, rightMax, leftSum+rightSum

}

func Max(x, y int) int {
	if x > y {
		return x
	}
	return y
}