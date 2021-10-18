class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        x = []
        for i in sorted(intervals, key=lambda x: x[0]):
            if len(x) == 0:
                x.append(i)
            elif i[0] <= x[-1][1]:
                # 如果新的 array 的左邊值小於 x 的右邊值表示兩個是 overlap，需要更新最大值
                x[-1][1] = max(i[1], x[-1][1])
            else:
                x.append(i)
        return x



s = Solution()
print(s.merge([[1,4],[2,5],[3,6]]))
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
print(s.merge([[1,4],[4,5]]))
