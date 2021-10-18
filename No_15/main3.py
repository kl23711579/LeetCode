class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        if n < 3:
            return []
        results = []
        for i in range(n):
            if nums[i] > 0:
                break
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            target = 0 - nums[i]
            s = i + 1
            e = n - 1
            for j in range(s, n):

