class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        if n < 3:
            return []
        results = []
        for i in range(0, n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    summary = nums[i] + nums[j]
                    summary += nums[k]
                    if summary == 0:
                        result = [nums[i], nums[j], nums[k]]
                        result.sort()
                        if result not in results:
                            results.append(result)
        return results

s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))
print(s.threeSum([]))
print(s.threeSum([[]]))
print(s.threeSum([1,2,3]))
print(s.threeSum([1,2]))
