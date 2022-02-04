class Solution(object):
    def oddEvenJumps(self, A):      # -----> O(n*n)
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A) # length of the array 
        odd = [-1] * n # [-1, -1, -1, ................. n times]
        even = [-1] * n # [-1, -1, -1, ................. n times]

        dp = [[0, 0] for _ in range(n)]  # [[0, 0], [0, 0], [0, 0], [0, 0]......... n times]

        dp[-1] = [1, 1]  # [[0, 0], [0, 0], [0, 0], ................ , [1, 1]]

        for i in range(n - 2 , -1, -1): 
            max_val = min(A[i + 1:]) - 1
            max_idx= -1
            min_idx= -1
            min_val = max(A[i + 1:]) + 1
            for j in range(i + 1, n):
                if A[i] >= A[j] and A[j] > max_val:
                    max_idx = j
                    max_val = A[j]
                if A[i] <= A[j] and A[j] < min_val:
                    min_idx = j
                    min_val = A[j]
            odd[i] = min_idx
            even[i] = max_idx

        ans = 1
        for k in range(n - 2, -1, -1):
            if even[k] != -1:
                dp[k][0] = dp[even[k]][1]  # even -> odd
            if odd[k] != -1:
                dp[k][1] = dp[odd[k]][0]  # odd -> even
            ans += dp[k][1]

        return ans


arr = [10, 13, 12, 14, 15]
obj = Solution()
print((obj.oddEvenJumps(arr)))
