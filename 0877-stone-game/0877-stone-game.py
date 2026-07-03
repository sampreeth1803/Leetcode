class Solution(object):
    def stoneGame(self, piles):
        dp = list(piles)
        for length in range(2, len(piles) + 1):
            dp = [max(piles[i] - dp[i + 1], piles[i + length - 1] - dp[i]) for i in range(len(piles) - length + 1)]
        return dp[0] > 0