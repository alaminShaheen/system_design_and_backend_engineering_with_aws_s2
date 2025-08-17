from typing import List


def maxProfit(self, prices: List[int]) -> int:
	dp = [[-1] * 2 for _ in range(len(prices) + 1)]

	# recursive top down TC -> O(2 ^ n), SC -> O(n)
	def recursive(index: int, bought: bool) -> int:
		# base case
		# I've exhausted looking at the array
		if index == len(prices):
			return 0
		# if I've already bought a stock before then need to sell
		if bought:
			# either sell at current price and be done (since I can only do 1 transaction)
			sell = prices[index]
			# or skip selling at current price for a better selling price ahead
			skip_sell = recursive(index + 1, bought)
			# max of whatever I do
			return max(sell, skip_sell)
		# if I've not bought any stocks before need to buy
		else:
			# either buy at current price
			buy = -prices[index] + recursive(index + 1, True)
			# or skip buying at current price for a better buying price ahead
			skip_buy = recursive(index + 1, bought)
			# max of whatever I do
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
		# states depend on only whether I've bought or not. Don't need the index state.
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
