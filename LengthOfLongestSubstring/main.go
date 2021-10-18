package main

import "fmt"

func main() {
	fmt.Println(lengthOfLongestSubstring("abb"))
}

func lengthOfLongestSubstring(s string) int {
	if len(s) == 0 {
		return 0
	} else if len(s) == 1 {
		return 1
	}

	var indexArray []int
 	var charArray []string
	max := 0
	index := 0
	findInAry := false
	prePoint := -1

	for i := 0; i < len(s); i++ {
		findInAry = ContainsKey(charArray, string(s[i]))

		if !findInAry {
			indexArray = append(indexArray, i)
			charArray = append(charArray, string(s[i]))
		} else {
			index = FindCharInAry(charArray, string(s[i]))
			prePoint = Max(indexArray[index], prePoint) // because prepoint cannot backward
			indexArray[index] = i
		}
		max = Max(max, i - prePoint)
	}
	return max
}

func FindCharInAry(charArray []string, key string) int {
	for i := 0; i < len(charArray); i++ {
		if charArray[i] == key {
			return i
		}
	}

	return 0
}

func ContainsKey(charArray []string, key string) bool {
	for _, item := range charArray {
		if item == key {
			return true
		}
	}
	return false
}

func Max(x, y int) int {
	if x > y {
		return x
	}

	return y
}
