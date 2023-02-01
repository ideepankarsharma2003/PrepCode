class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        minDist = 10000000
        ansIdx = -1
        l = len(points)
        for i in range(l):
            if points[i][0] == x or points[i][1] == y:
                dist = abs(x-points[i][0]) + abs(y - points[i][1])
                # print(dist)
                if dist < minDist:
                    ansIdx = i
                    minDist = dist
        return ansIdx
