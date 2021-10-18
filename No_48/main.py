class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        def swap(index1, index2, matrix) -> list[list[int]]:
            temp = matrix[index1[0]][index1[1]]
            matrix[index1[0]][index1[1]] = matrix[index2[0]][index2[1]]
            matrix[index2[0]][index2[1]] = temp
            return matrix

        n = len(matrix)
        half = int(n/2)
        # swap symmetry
        for i in range(half):
            for j in range(n):
                matrix = swap([i,j], [n-i-1,j], matrix)
        # swap diagonal
        for i in range(n):
            for j in range(n):
                if i == j:
                    break
                else:
                    matrix = swap([i,j],[j,i],matrix)

    
    def show_result(self, matrix) -> None:
        for i in matrix:
            for j in i:
                print("%2d " % j, end="")
            print()

s = Solution()
s.rotate([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
s.rotate([[1,2,3],[4,5,6],[7,8,9]])
s.rotate([[1,2],[3,4]])
s.rotate([[1]])
