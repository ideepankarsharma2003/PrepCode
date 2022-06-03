class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        l = len(coordinates)
        if l == 2:
            return True

        dy1 = coordinates[1][1]-coordinates[0][1]
        dx1 = coordinates[1][0]-coordinates[0][0]
        dy2 = coordinates[2][1]-coordinates[1][1]
        dx2 = coordinates[2][0]-coordinates[1][0]

        # print(m)
        for i in range(l-2):
            # x= coordinates[i+1][0]-coordinates[i+0][0]
            # y= coordinates[i+1][1]-coordinates[i+0][1]
            # if x!= 0:
            #     mDash= y/x
            #     print('mDash=', mDash)
            #     if mDash!=m:
            #         return False
            dx1 = coordinates[i+1][0]-coordinates[i+0][0]
            dy1 = coordinates[i+1][1]-coordinates[i+0][1]
            dx2 = coordinates[i+2][0]-coordinates[i+1][0]
            dy2 = coordinates[i+2][1]-coordinates[i+1][1]

            if dy2*dx1 != dy1*dx2:
                return False

            # if xD!=0:
            #     mD= yD/xD
            # else:
            #     mD=0
            # cD= coordinates[i+0][1]- mD*coordinates[i+0][0]
            # if c!=cD:
            #     return False

            # if xD!=x:
            #     return False
        return True
