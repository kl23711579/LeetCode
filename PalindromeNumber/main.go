package main

import (
	"fmt"
)

func main() {
	num := 0
	_, err := fmt.Scanf("%d", &num)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(isPalindrome(num))
}

func isPalindrome(num int) bool {
	if num < 0 {
		return false
	}

	if num == 0 {
		return true
	}

	origin := num
	reverse := 0

	for num > 0 {
		reverse = reverse*10 + (num % 10)
		num /= 10
	}

	fmt.Println(origin)
	fmt.Println(reverse)

	return origin == reverse
}
