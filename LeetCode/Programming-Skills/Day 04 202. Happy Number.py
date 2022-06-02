class Solution:
    def isHappy(self, n: int) -> bool:
        l = [int(i) for i in str(n)]
        s = sum([i**2 for i in l])
        while(len(l) > 1):
            s = sum([i**2 for i in l])
            l = [int(i) for i in str(s)]
            # print(l)
        if s == 1:
            return True
        i = 100
        m = []
        while i > 0:
            i -= 1
            s = sum([i**2 for i in l])
            if s in m:
                if 1 in m:
                    return True
                else:
                    return False
            m.append(s)
            l = [int(i) for i in str(s)]
            # print(s)
