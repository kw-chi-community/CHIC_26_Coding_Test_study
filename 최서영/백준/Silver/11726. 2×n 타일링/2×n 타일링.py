# 방법 1 : 마지막에 세로 타일 1개
# 앞에까지는 2x(n-1) -> 경우의 수 : dp[n-1]

# 방법 2 : 마지막에 가로 타일 2개
# 앞에까지는 2×(n-2) -> 경우의 수 : dp[n-2]

import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n + 1)

dp[1] = 1

if n >= 2:
    dp[2] = 2
    
for i in range(3, n + 1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007
    
print(dp[n])