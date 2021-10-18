class Solution:
    def canJump(self, nums:list[int]) -> bool:
        explored = [False] * len(nums)
        def helper(index, nums) -> bool:
            explored[index] = True
            if index >= len(nums)-1:
                return True
            steps = nums[index]
            while steps > 0:
                if explored[index+steps]:
                    break
                if helper(index+steps, nums):
                    return True
                steps -= 1
            return False
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False
        return helper(0, nums)

s = Solution()
print(s.canJump([1,2,3]))
print(s.canJump([1,0,3]))
print(s.canJump([2,3,1,1,4]))
print(s.canJump([3,2,1,0,4]))
print(s.canJump([0]))
print(s.canJump([10]))
print(s.canJump([1,1,1,1,1,1,1,0]))
print(s.canJump([1,1,1,1,1,1,0,1]))
print(s.canJump([2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]))
