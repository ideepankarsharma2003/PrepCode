class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        l= []
        lm= len(mat)
        x= lm-1
        for i in range(lm):
            l.append(mat[i][i])
            if x!=i:
                l.append(mat[i][x])
            x-=1
            
        # l= set(l)
        # l= list(l)
        return sum(l)

        