package main

func twoSum(nums []int, target int) []int {
	m := make(map[int]int)

	for index, item := range nums {
		num := target - item
		if elem, ok := m[num]; ok {
			return []int{elem, index}
		} else {
			m[item] = index
		}
	}

	return []int{}
}
