class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        results = []
        if n < 3: 
            return results
        for i in range(n):
            if nums[i] > 0:
                break
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            s, e = i+1, n-1
            target = 0-nums[i]
            while s < e:
                if (nums[s]+nums[e]) == target:
                    results.append([nums[i], nums[s], nums[e]])
                    s = s + 1
                    e = e - 1
                    while s < e and nums[s] == nums[s-1]:
                        s = s + 1
                    while s < e and nums[e] == nums[e+1]:
                        e = e - 1
                elif nums[s]+nums[e] < target:
                    s = s + 1
                    while s < e and nums[s] == nums[s-1]:
                        s = s + 1
                elif nums[s]+nums[e] > target:
                    e = e - 1
                    while s < e and nums[e] == nums[e+1]:
                        e = e - 1

        return results


s = Solution()
print(s.threeSum([0,0,0]))
# -4, -1, -1, 0, 1, 2
print(s.threeSum([-1,0,1,2,-1,-4]))
print(s.threeSum([]))
print(s.threeSum([[]]))
print(s.threeSum([1,2,3]))
print(s.threeSum([1,2]))
