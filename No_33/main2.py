class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def find_rot(s, e , nums) -> int:
            if s == e:
                return s
            mid = int((s+e)/2)
            # pivot in right side
            if nums[mid] > nums[e]:
                return find_rot(mid+1, e, nums)
            # in left side
            else:
                return find_rot(s, mid, nums)

        def helper(s, e, nums, target) -> int:
            if s >= e and nums[s] != target:
                return -1
            mid = int((s+e)/2)
            if nums[mid] == target:
                return mid
            # left
            elif nums[mid] > target:
                return helper(s, mid-1, nums, target)
            elif nums[mid] < target:
                return helper(mid+1, e, nums, target)

    
        n = len(nums)
        pivot = find_rot(0, n-1, nums)

        if target == nums[pivot]:
            return pivot
        elif target > nums[n-1]: # in the left of pivot
            return helper(0, pivot, nums, target)
        else:
            return helper(pivot, n-1, nums, target)

s = Solution()
print(s.search([4,5,6,7,8,1,2], 0))
print(s.search([5,6,7,0,1,2,4], 6))
print(s.search([6,7,0,1,2,4,5], 1))
print(s.search([7,0,1,2,4,5,6], 7))
print(s.search([0,1,2,4,5,6,7], 7))
print(s.search([1,2,4,5,6,7,0], 7))
print(s.search([2,4,5,6,7,0,1], 6))
print(s.search([4,5,6,7,0,1,2,3], 5))
print(s.search([1],0))
print(s.search([2],2))
print(s.search([1,2],2))
print(s.search([1,2],3))
