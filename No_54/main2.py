class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        '''
        Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        Output: [1,2,3,4,8,12,11,10,9,5,6,7]
        '''
        self.show_result(matrix)
        explored = []
        cols = len(matrix[0])
        rows = len(matrix)
        point = [0, 0]
        result = []
        for i in range(rows):
            explored.append([])
            for _ in range(cols):
                explored[i].append(True)
        
        while len(result) < rows*cols:
            while True:
                if explored[point[0]][point[1]]:
                    result.append(matrix[point[0]][point[1]])
                    explored[point[0]][point[1]] = False
                if point[1]+1 < cols and explored[point[0]][point[1]+1]:
                    point = [point[0], point[1]+1]
                else:
                    break
            while True:
                if explored[point[0]][point[1]]:
                    result.append(matrix[point[0]][point[1]])
                    explored[point[0]][point[1]] = False
                if point[0]+1 < rows and explored[point[0]+1][point[1]]:
                    point = [point[0]+1, point[1]]
                else:
                    break
            while True:
                if explored[point[0]][point[1]]:
                    result.append(matrix[point[0]][point[1]])
                    explored[point[0]][point[1]] = False
                if point[1]-1 >= 0 and explored[point[0]][point[1]-1]:
                    point = [point[0], point[1]-1]
                else:
                    break
            while True:
                if explored[point[0]][point[1]]:
                    result.append(matrix[point[0]][point[1]])
                    explored[point[0]][point[1]] = False
                if point[0]-1 >= 0 and explored[point[0]-1][point[1]]:
                    point = [point[0]-1, point[1]]
                else:
                    break
        return result

    def show_result(self, matrix) -> None:
        for i in matrix:
            for j in i:
                print("%2d " % j, end="")
            print()

s = Solution()
print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
print(s.spiralOrder([[1,2,3],[5,6,7],[9,10,11]]))
print(s.spiralOrder([[1,2,3,2,1],[5,6,7,5,5],[9,10,11,12,14],[9,10,11,12,14],[9,10,11,12,14],[9,10,11,12,14],[9,10,11,12,14]]))
print(s.spiralOrder([[1]]))
print(s.spiralOrder([[1,2,3]]))
print(s.spiralOrder([[1,1],[2,2]]))