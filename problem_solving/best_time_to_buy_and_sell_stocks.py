from typing import List


def maxProfit(self, prices: List[int]) -> int:
	dp = [[-1] * 2 for _ in range(len(prices) + 1)]

	# # recursive top down TC -> O(2 ^ n), SC -> O(n)
	def recursive(index: int, bought: bool) -> int:
		if index == len(prices):
			return 0

		if bought:
			sell = prices[index]
			skip_sell = recursive(index + 1, bought)
			return max(sell, skip_sell)
		else:
			buy = -prices[index] + recursive(index + 1, True)
			skip_buy = recursive(index + 1, bought)
			return max(buy, skip_buy)

	# return max(0, recursive(0, False))

	# recursive memoized top down TC -> O(2 * (n + 1)) ≈ O(n), SC -> O(2 * n + n (auxiliary)) ≈ O(n)
	def recursive_memoized(index: int, bought: int, dp: List[List[int]]) -> int:
		if index == len(prices):
			return 0
		elif dp[index][bought] == -1:
			if bought:
				sell = prices[index]
				skip_sell = recursive_memoized(index + 1, bought, dp)
				dp[index][bought] = max(sell, skip_sell)
			else:
				buy = -prices[index] + recursive_memoized(index + 1, True, dp)
				skip_buy = recursive_memoized(index + 1, bought, dp)
				dp[index][bought] = max(buy, skip_buy)
		return dp[index][bought]

	# return max(0, recursive_memoized(0, False, dp))

	# iterative top down TC -> O(2 * (n + 1)) ≈ O(n), SC -> O(2 * (n + 1)) ≈ O(n)
	def iterative():
		for index in range(len(prices), -1, -1):
			for bought in range(2):
				if index == len(prices):
					dp[index][bought] = 0
					continue
				if bought:
					sell = prices[index]
					skip_sell = dp[index + 1][bought]
					dp[index][bought] = max(sell, skip_sell)
				else:
					buy = -prices[index] + dp[index + 1][1]
					skip_buy = dp[index + 1][bought]
					dp[index][bought] = max(buy, skip_buy)
		return dp[0][0]

	# return max(0, iterative())

	# iterative space optimized top down TC -> O(2 * (n + 1)) ≈ O(n), SC -> O(2 + 2) ≈ O(1)
	def optimized_iterative():
		dp = [-1] * 2
		temp = [-1] * 2
		for index in range(len(prices), -1, -1):
			for bought in range(2):
				if index == len(prices):
					dp[bought] = 0
					continue
				if bought:
					sell = prices[index]
					skip_sell = temp[bought]
					dp[bought] = max(sell, skip_sell)
				else:
					buy = -prices[index] + temp[1]
					skip_buy = temp[bought]
					dp[bought] = max(buy, skip_buy)
			temp = dp[:]
		return dp[0]

	return max(0, optimized_iterative())
