def coin_change(coins: list[int], amount: int) -> list[int] | None:
    omega: list[int] = [0] * (amount + 1)  # creates a list with 0 and then applies the formula to calculate the minimum number of coins needed for each amount (amount + 1) times
    dp: list[list[int]] = [omega] * (amount + 1)  # the vlue of dp[i] is the minimum number of coins needed to make change for amount i
    dp[0] = []  # base case: no coins are needed to make change
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                candidate: list[int] = dp[i - coin] + [coin]  # candidate is the list of coins used to make change for amount i - coin, plus the current coin
                if len(candidate) < len(dp[i]) or not dp[i]:  # if the candidate list is shorter than the current list of coins used to make change for amount i, or if there are no coins used yet
                    dp[i] = candidate  # update the list of coins used to make change for amount i
    if dp[amount] is omega:  # if the list of coins used to make change for amount is still the same as the initial list, then it is not possible to make change for that amount
        return None
    
    # return dp[amount]  # return the list of coins used to make change for amount
    return sorted(dp[amount], reverse=True)

if __name__ == "__main__":
    print(coin_change([1, 2, 5, 10, 20], 27)) 
    print(coin_change([1, 2, 5, 10, 20], 33)) 
    print(coin_change([1, 2, 5, 10, 20], 9)) 
    print()
    print(coin_change([2, 5], 6)) 
    print(coin_change([2, 5], 3)) 