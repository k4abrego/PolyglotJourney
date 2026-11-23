def fibo_recursive(n):
    if n <= 1:
        return n
    else:
        return fibo_recursive(n - 1) + fibo_recursive(n - 2)

def fibo_dp(n: int) -> int: #more quick and efficient than the recursive method, as it uses dynamic programming to store previously calculated values
    if n == 0:
        return 0
    dp: list[int] = [0] * (n + 1) #creates a list with 0 and then applies the formula to calculate the fibonacci number (n + 1) times
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

if __name__ == "__main__":
    # print(fibo_recursive(10))  #55
    print(fibo_dp(40))