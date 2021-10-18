package main

func searchInsert(nums []int, target int) int {
	if len(nums) == 0 {
		return 0
	}

	for index, item := range nums {
		if target <= item {
			return index
		}
	}

	return len(nums)
}
