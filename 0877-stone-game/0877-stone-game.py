class Solution(object):
    def stoneGame(self, piles):
        n = len(piles)
        
        # dp[i] will store the maximum relative score advantage a player 
        # can get from the subarray starting at index 'i'.
        # Base case: When subarray length is 1, the player just takes that pile.
        dp = list(piles)
        
        # Iterate through all possible subarray lengths starting from 2 up to n
        for length in range(2, n + 1):
            
            # Create a temporary array to hold the updates for the current length.
            # This prevents overwriting values we still need in the loop.
            next_dp = [0] * (n - length + 1)
            
            # Check every valid starting index 'i' for the current subarray length
            for i in range(n - length + 1):
                # Calculate the ending index 'j' of the current subarray
                j = i + length - 1
                
                # Option 1: Take the leftmost pile (piles[i]).
                # The opponent then gets the remaining subarray piles[i+1 ... j].
                # dp[i+1] currently holds the opponent's max advantage for that remaining part.
                pick_left = piles[i] - dp[i + 1]
                
                # Option 2: Take the rightmost pile (piles[j]).
                # The opponent then gets the remaining subarray piles[i ... j-1].
                # dp[i] currently holds the opponent's max advantage for that remaining part.
                pick_right = piles[j] - dp[i]
                
                # Choose the option that gives the current player the maximum advantage
                next_dp[i] = max(pick_left, pick_right)
            
            # Move the calculated row up to become the baseline for the next length
            dp = next_dp
            
        # dp[0] now represents the final score advantage for the full array piles[0 ... n-1].
        # If Alice's score minus Bob's score is greater than 0, Alice wins.
        return dp[0] > 0
