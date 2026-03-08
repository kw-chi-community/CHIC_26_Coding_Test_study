N = int(input())

answer = 0

for M in range(1, N+1):
    s = M + sum(map(int, str(M)))
    if s == N:
        answer = M
        break
        
print(answer)