#!/usr/bin/python3
"""
Making Change
"""


def makeChange(coins, total):
    """Making Change"""

    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            if dp[i] == dp[i - coin] + 1:
                continue
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
