class Solution:
    def getRow(self, idx: int) -> List[int]:
        tri = [[1]*(i+1) for i in range(idx + 1)]
        for i in range(idx + 1):
            for j in range(i+1 // 2):
                if j != 0:
                    tri[i][i-j] = tri[i][j] = tri[i-1][j-1] + tri[i-1][j]      
        return tri[idx]


        

        