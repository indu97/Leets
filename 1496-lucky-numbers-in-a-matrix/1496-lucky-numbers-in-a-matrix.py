class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        res = []
        for i in range(0, m):
            row_min = matrix[i][0]
            store_j = 0
            for j in range(1, n):
                if row_min > matrix[i][j]:
                    row_min = matrix[i][j]
                    store_j = j
            lucky_flag = 0
            for k in range(0, m):
                if row_min < matrix[k][store_j]:
                    lucky_flag = 1
                    break
            if lucky_flag == 0:
                res.append(matrix[i][store_j])
        return res
                
