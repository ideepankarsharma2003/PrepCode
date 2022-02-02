# O(n log n)

class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        n = len(A)
        # odd/even[i] -- start at i, next jump is odd/even
        odd, even = [False] * n, [False] * n
        odd[-1], even[-1] = True, True

        # sort by value then by index
        Asort = sorted([(x, i) for i, x in enumerate(A)])
        Asort_rev = sorted([(-x, i) for i, x in enumerate(A)])

        # find the jump-to location of each index
        oddjump = self.findjump(Asort)
        evenjump = self.findjump(Asort_rev)

        n_good = 1
        # try all starting locations, both odd and even
        # make one jump, use the solution of the jump-to location
        for i in range(n-2, -1, -1):  # n-1,n-2...1,0
            j = oddjump[i]
            if j is not None:
                odd[i] = even[j]
            # if j is None, then no legal jump

            j = evenjump[i]
            if j is not None:
                even[i] = odd[j]

            if odd[i]:
                n_good += 1
        return n_good

    def findjump(self, Asort):
        # monotonic stack
        stack = []
        # the jump-to index of each index
        jumpto = [None] * len(Asort)

        for _, i in Asort:
            # pop the indexes smaller than current
            # point th jump-to of these indexes to current
            while stack and stack[-1] < i:
                jumpto[stack.pop()] = i
            # push into stack
            stack.append(i)

        return jumpto
