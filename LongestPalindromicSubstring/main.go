package main

import "fmt"

func main() {
	fmt.Println(longestPalindrome("abawerttrewbccb"))
}

func longestPalindrome(s string) string {
	if len(s) == 0 {
		return ""
	}
	longString := string(s[0])
	for i := 0; i < len(s); i++ {
		for j := len(s)-1; j > i; j-- {
			if check(s, i, j) {
				if j - i + 1 > len(longString) {
					longString = s[i:j+1]
				}
				break
			}
		}
	}
	return longString
}

func check(s string, i, j int) bool {
	if len(s) == 1 {
		return true
	}

	for ; j > i ;i++{
		if s[i] != s[j] {
			return false
		}
		j--
	}

	return true
}