import sys

def fib_bottom_up(n):
    if n == 0:
        return 0
    fib = [0, 1]  # 초기값 세팅
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]


# def fibo(n):
# 	dp = [0] * (n + 1)
# 	dp[0] = 0
# 	dp[1] = 1
	
# 	for i in range(2, n+1):
# 		dp[i] = dp[i-1] + dp[i-2]
	
# 	return dp[n]


n= int(sys.stdin.readline())
print(fib_bottom_up(n))