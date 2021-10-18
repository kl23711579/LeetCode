'''
No 39
Combination Sum
25/11
'''

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        n = len(candidates)
        def helper(result, summary, index):
            if summary > target:
                return
            
            if summary == target:
                ans.append(result)
                return

            for i in range(index, n):
                helper(result + [candidates[i]], summary+candidates[i], i)

        helper([], 0, 0)
        return ans


s = Solution()

print(s.combinationSum([1,2], 5))