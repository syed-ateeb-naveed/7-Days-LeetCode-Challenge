class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        dp = [[float("inf")] * (len(w2) + 1) for i in range(len(w1) + 1)]

        for j in range(len(w2) + 1):
            dp[len(w1)][j] = len(w2) - j
        for i in range(len(w1) + 1):
            dp[i][len(w2)] = len(w1) - i


        for i in range(len(w1) - 1, -1, -1):
            for j in range(len(w2) - 1, -1, -1):
                if w1[i] == w2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
    
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])


        return dp[0][0]