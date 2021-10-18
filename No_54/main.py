class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        '''
        Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        Output: [1,2,3,4,8,12,11,10,9,5,6,7]
        '''
        s.show_result(matrix)
        bottom = len(matrix)
        up = 0
        right = len(matrix[0])
        left = 0
        col = 0
        row = 0
        results = []
        rows, cols = bottom, right
        while len(results) < rows*cols:
            # right
            while col < right:
                print("R")
                results.append(matrix[row][col])
                col += 1
            col -= 1
            row += 1
            up += 1
            # down
            while row < bottom:
                print("D")
                results.append(matrix[row][col])
                row += 1
            row -= 1
            col -= 1
            right -= 1
            # left
            while col >= left:
                print("L")
                results.append(matrix[row][col])
                col -= 1
            col += 1
            row -= 1
            bottom -= 1
            # up
            while row >= up:
                print("U")
                results.append(matrix[row][col])
                row -= 1
            row += 1
            col += 1
            left += 1
        return results

    def show_result(self, matrix) -> None:
        for i in matrix:
            for j in i:
                print("%2d " % j, end="")
            print()

s = Solution()
print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
print(s.spiralOrder([[1,2,3],[5,6,7],[9,10,11]]))
