class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_curr, max_sofar = 0, 0
        for i in range(1, len(prices)):
            max_curr = max(0, max_curr+prices[i]-prices[i-1])
            max_sofar = max(max_sofar, max_curr)
                    
        return max_sofar


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7,6,4,3,1]))
    print()
    print(s.maxProfit([7,1,5,3,6,4]))
    print(s.maxProfit([7,1,5,3,6,4,10,13,19,11,12,2,20]))