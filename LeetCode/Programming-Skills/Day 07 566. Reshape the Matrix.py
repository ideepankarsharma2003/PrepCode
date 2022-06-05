class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        l = [j for i in mat for j in i]
        # print(f'l= {l}')

        # r = 2
        if len(mat)*len(mat[0]) != r*c:
            return mat
        # lDash= [[]]*r
        # print(f'r= {r}, c= {c}')

        # lDash[0].append(1)
        lDash = []

        # rc = 0
        cc = 0
        temp = []
        for i in range(len(l)):
            if cc >= c:
                cc = 0
                lDash.append(temp)
                temp = []

            temp.append(l[i])
            # print(temp)
            cc += 1

        lDash.append(temp)

        return lDash
