import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

# 누적합 배열
prefix = [0] * (N+1)
# prefix[i] = 1번부터 i번까지의 합

for i in range(1, N+1):
    prefix[i] = prefix[i-1] + numbers[i-1]
    
# 구간 합 처리
for _ in range(M):
    i, j = map(int, input().split())
    print(prefix[j] - prefix[i-1])