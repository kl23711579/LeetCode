class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m, n = m-1, n-1
        up = m+n
        down = min(m, n)
        u = 1
        d = 1
        while down > 0:
            u *= up
            d *= down
            up -= 1
            down -= 1
        
        return int(u/d)

s = Solution()
print(s.uniquePaths(3,3))
print(s.uniquePaths(1, 1))
print(s.uniquePaths(7,3))
print(s.uniquePaths(2,1))
