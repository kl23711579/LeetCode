class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def helper(s, e, nums, target) -> int:
            if target == nums[e]:
                return e
            elif target == nums[s]:
                return s
            mid = int((s+e)/2)
            print(f"s={s}, e={e}, mid={mid}")
            if target == nums[mid]:
                return mid
            if s == e:
                return -1
            elif target < nums[mid] and target < nums[e]:
                return helper(mid+1, e, nums, target)
            elif target < nums[mid] and target > nums[s]:
                return helper(s, mid, nums, target)
            elif target > nums[mid] and target > nums[e]:
                return helper(mid+1, e, nums, target)
            elif target > nums[mid] and target < nums[s]:
                return helper(s, mid, nums, target)
            else:
                return -1

        n = len(nums)
        return helper(0, n-1, nums, target)

s = Solution()
#print(s.search([4,5,6,7,0,1,2], 0))
#print(s.search([4,5,6,7,0,1,2], 1))
#print(s.search([4,5,6,7,0,1,2], 2))
#print(s.search([4,5,6,7,0,1,2], 3))
#print(s.search([4,5,6,7,0,1,2], 4))
#print(s.search([4,5,6,7,0,1,2], 5))
print(s.search([4,5,6,7,0,1,2], 6))
#print(s.search([4,5,6,7,0,1,2], 7))
#print(s.search([4,5,6,7,0,1,2], 8))
# 4 5 6 7 0 1 2

