package main

import "strings"

func lengthOfLastWord(s string) int {
	if len(s) == 0 {
		return 0
	}

	sArr := strings.Split(s, " ")

	for i := len(sArr)-1; i >= 0; i-- {
		if len(sArr[i]) != 0 {
			return len(sArr[i])
		}
	}
	return 0
}
