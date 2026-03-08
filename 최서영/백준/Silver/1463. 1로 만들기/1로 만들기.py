import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * (N + 1)
# dp[i] = i를 1로 만드는 최소 연산 횟수

for i in range(2, N+1):
    # 1을 빼는 경우
    dp[i] = dp[i-1] + 1
    
    # 2로 나누는 경우
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
        
    # 3으로 나누는 경우
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
        # dp[i//3] + 1에서 +1은 이미 i → i/3 이라는 연산을 한 번 했기 때문에
        
print(dp[N])