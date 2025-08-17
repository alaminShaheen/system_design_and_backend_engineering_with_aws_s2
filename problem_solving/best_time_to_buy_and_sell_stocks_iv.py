from typing import List


def maxProfit(self, k: int, prices: List[int]) -> int:
	max_transactions = k
	dp = [[[-1] * (max_transactions + 1) for _ in range(2)] for _ in range(len(prices) + 1)]

	# recursive top down TC -> O(2^n), SC -> O(n), n = len(prices)
	def recursive(index: int, bought: bool, transactions: int) -> int:
		if transactions == 0 or index == len(prices):
			return 0

		if bought:
			sell = prices[index] + recursive(index + 1, False, transactions - 1)
			skip_sell = recursive(index + 1, bought, transactions)
			return max(sell, skip_sell)
		else:
			buy = -prices[index] + recursive(index + 1, True, transactions)
			skip_buy = recursive(index + 1, bought, transactions)
			return max(buy, skip_buy)

	# return recursive(0, False, k)

	# recursive memoized top down TC -> O(2 * (k + 1) * (n + 1)) ≈ O(n * k), SC -> O(2 * (k + 1) * (n + 1) + n (auxiliary)) ≈ O(n * k), where n = len(prices), k = max_transactions
	def recursive_memoized(index: int, bought: int, transactions: int, dp: List[List[List[int]]]) -> int:
		if transactions == 0 or index == len(prices):
			return 0
		elif dp[index][bought][transactions] == -1:
			if bought:
				sell = prices[index] + recursive_memoized(index + 1, False, transactions - 1, dp)
				skip_sell = recursive_memoized(index + 1, bought, transactions, dp)
				dp[index][bought][transactions] = max(sell, skip_sell)
			else:
				buy = -prices[index] + recursive_memoized(index + 1, True, transactions, dp)
				skip_buy = recursive_memoized(index + 1, bought, transactions, dp)
				dp[index][bought][transactions] = max(buy, skip_buy)
		return dp[index][bought][transactions]

	# return recursive_memoized(0, 0, 2, dp)

	# iterative bottom up TC -> O(2 * (k + 1) * (n + 1)) ≈ O(n * k), SC -> O(2 * (k + 1) * (n + 1)) ≈ O(n * k), where n = len(prices), k = max_transactions
	def iterative() -> int:
		for index in range(len(prices), -1, -1):
			for bought in range(2):
				for transactions in range(max_transactions + 1):
					if transactions == 0 or index == len(prices):
						dp[index][bought][transactions] = 0
						continue
					if bought:
						sell = prices[index] + dp[index + 1][0][transactions - 1]
						skip_sell = dp[index + 1][bought][transactions]
						dp[index][bought][transactions] = max(sell, skip_sell)
					else:
						buy = -prices[index] + dp[index + 1][1][transactions]
						skip_buy = dp[index + 1][bought][transactions]
						dp[index][bought][transactions] = max(buy, skip_buy)
		return dp[0][0][-1]

	# return iterative()

	# iterative space optimized bottom up TC -> O(2 * (k + 1) * (n + 1)) ≈ O(n), SC -> O(2 * (k + 1)) ≈ O(k), where n = len(prices), k = max_transactions
	def iterative_optimized() -> int:
		dp = [[-1] * (max_transactions + 1) for _ in range(2)]
		temp = [[-1] * (max_transactions + 1) for _ in range(2)]
		for index in range(len(prices), -1, -1):
			for bought in range(2):
				for transactions in range(max_transactions + 1):
					if transactions == 0 or index == len(prices):
						dp[bought][transactions] = 0
						continue
					if bought:
						sell = prices[index] + temp[0][transactions - 1]
						skip_sell = temp[bought][transactions]
						dp[bought][transactions] = max(sell, skip_sell)
					else:
						buy = -prices[index] + temp[1][transactions]
						skip_buy = temp[bought][transactions]
						dp[bought][transactions] = max(buy, skip_buy)
			for i in range(2):
				temp[i] = dp[i][:]
		return dp[0][-1]

	return iterative_optimized()
