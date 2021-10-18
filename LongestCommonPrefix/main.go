package main

import (
	"fmt"
)

func main() {
	stringAry := []string{"a"}
	fmt.Println(longestCommonPrefix(stringAry))
}

func longestCommonPrefix(strs []string) string {
	//len := len(strs[0])

	tail := 0

	if len(strs) == 0 {
		return ""
	}

	if len(strs) == 1 {
		return strs[0]
	}

	for _, item := range strs {
		if item == "" {
			return ""
		}
	}

	length := len(strs[1])
	// find first common prifix
	for index := range strs[0] {
		if index >= length {
			break
		}
		if strs[0][index] == strs[1][index] {
			tail = index + 1
		} else {
			if index == 0 {
				return ""
			} else {
				break
			}
		}
	}

	commonPrefix := strs[0][0:tail]
	for index, item := range strs {
		if index == 0 || index == 1 {
			continue
		}

		length = len(item)
		tail = 0

		for index2 := range commonPrefix {
			if index2 >= length {
				break
			}
			if commonPrefix[index2] == strs[index][index2] {
				tail = index2 + 1
			} else {
				if index2 == 0 {
					return ""
				} else {
					break
				}
			}
		}

		commonPrefix = commonPrefix[0:tail]
	}

	return commonPrefix
}
