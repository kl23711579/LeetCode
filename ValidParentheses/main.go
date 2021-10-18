package main

import (
	"fmt"
)

func main() {
	str := ""

	fmt.Scanf("%s", &str)

	fmt.Println(validParenthese(str))
}

func validParenthese(str string) bool {
	sign := make([]rune, 0)
	i := 0
	for _, item := range str {
		if item == 123 || item == 91 || item == 40 {
			sign = append(sign, item)
			i++
		} else if item == 41 { // )
			length := len(sign)
			if length == 0 {
				return false
			}
			if sign[length-1] != 40 {
				return false
			} else {
				sign = sign[0 : length-1]
				i--
			}
		} else if item == 93 { // ]
			length := len(sign)
			if length == 0 {
				return false
			}
			if sign[length-1] != 91 {
				return false
			} else {
				sign = sign[0 : length-1]
				i--
			}
		} else if item == 125 { // }
			length := len(sign)
			if length == 0 {
				return false
			}
			if sign[length-1] != 123 {
				return false
			} else {
				sign = sign[0 : length-1]
				i--
			}
		}
	}

	length := len(sign)
	if length == 0 {
		return true
	} else {
		return false
	}
}
