class Solution:
    def numDecoding(self, s: str) -> int:
        if len(s) == 0:
            return 0
        dp = [0] * (len(s)+1)
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1
        for i in range(2, len(s)+1):
            # this word
            first = int(s[i-1:i])
            print("first: %d" % first)
            if first <= 9 and first >= 1:
                 dp[i] += dp[i-1]
            # this word + previous word
            if s[i-2] != '0':
                second = int(s[i-2:i])
                if second <= 26 and second >= 10:
                    dp[i] += dp[i-2]

        print(dp)

        return dp[len(s)]

s = Solution()
print(s.numDecoding("12"))
print(s.numDecoding("1229"))
print(s.numDecoding("1202"))
print(s.numDecoding("226"))
print(s.numDecoding("0"))
print(s.numDecoding("202"))
print(s.numDecoding("022"))
