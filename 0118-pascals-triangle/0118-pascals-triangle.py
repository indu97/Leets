class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pt = [[1]]
        for i in range(1,numRows):
            if i == 1:
                k = [1,1]
                pt.append(k)
            else:
                temp = []
                temp.append(1)
                for j in range(1,i):
                    temp.append(pt[i-1][j-1] + pt[i-1][j])
                temp.append(1)
                pt.append(temp)
        return pt
