package main

import (
	"fmt"
	"strconv"
)

func main() {
	fmt.Println(countAndSay(10))
}

func countAndSay(n int) string {
	str := "1"
	if n == 1 {
		return str
	}

	for i := 2; i <= n; i++ {
		count := 1
		newStr := ""
		if len(str) == 1 {
			newStr = "11"
		} else {
			for j := 1; j < len(str); j++ {
				if str[j] != str[j-1] {
					newStr += strconv.Itoa(count) + string(str[j-1])
					count = 1
				} else {
					count++
				}
			}
			newStr += strconv.Itoa(count) + string(str[len(str)-1])
		}
		str = newStr
	}
	return str
}
