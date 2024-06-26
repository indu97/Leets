class Solution:
    def getRow(self, idx: int) -> List[int]:
        tri = []

        for i in range(idx+1):
            tri.append([])
            for j in range(i+1):
                if j == 0 or j == i:
                    #tri[i][j] = 1
                    tri[i].append(1)
                else:
                    tri[i].append(tri[i-1][j-1] + tri[i-1][j])
        return tri[idx]

        