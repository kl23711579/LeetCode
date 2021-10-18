package main

import (
	"fmt"
	"math"
)

func main() {
	num := 0
	_, err := fmt.Scanf("%d", &num)
	if err != nil {
		fmt.Println(err)
		return
	}

	// 先判斷正負號並記起來
	sign := true
	if num < 0 {
		sign = false
		num = num * -1
	}
	multi := 0
	tempnum := num
	for tempnum >= 10 {
		tempnum /= 10
		multi++
	}

	result := 0
	for ; multi > 0; multi-- {
		result += (num % 10) * multTen(multi)
		num /= 10
	}
	result += num
	if !sign {
		result *= -1
	}

	if result > math.MaxInt32 || result < math.MinInt32 {
		result = 0
	}

	fmt.Println(result)
}

func multTen(n int) int {
	num := 1
	for i := 0; i < n; i++ {
		num *= 10
	}
	return num
}
