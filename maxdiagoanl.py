class Solution:
    def areaOfMaxDiagonal(self, dimensions: list[list[int]]) -> int:
        max_diagonal= 0
        max_area = 0
        #Step 1: calucalte diagonal
        for i in range(len(dimensions)):
            length = dimensions[i][0]
            width = dimensions[i][1]
            diagonal_sq = length**2 + width**2
            area = length * width
            if diagonal_sq > max_diagonal:
                max_diagonal = diagonal_sq
                max_area = area
            elif diagonal_sq == max_diagonal:
                if area > max_area:
                    max_area = area
            
        return max_area


sol = Solution()
dimensions =[[9,3],[8,6]]
print(sol.areaOfMaxDiagonal(dimensions))