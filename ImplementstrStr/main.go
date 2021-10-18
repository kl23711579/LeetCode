package main

import "fmt"

func main() {
	h := ""
	n := "hello"
	fmt.Println(strStr(h,n))
}

func strStr(haystack string, needle string) int {
	if needle == "" {
		return 0
	}

	hayLen := len(haystack)
	needleLen := len(needle)

	if needleLen > hayLen {
		return -1
	}

	j := 0
	for i := 0; i < hayLen; i++ {

		if haystack[i] == needle[j] {
			j++
			if j == needleLen {
				return i - j + 1
			}
		} else {
			i -= j
			j = 0
		}
	}
	return -1
}