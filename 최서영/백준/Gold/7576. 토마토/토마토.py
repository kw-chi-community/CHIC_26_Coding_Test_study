from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())

box = []
queue = deque() # BFS 탐색용 큐

for i in range(N):
    row = list(map(int, input().split()))
    box.append(row)
    for j in range(M):
        if row[j] == 1: # 1은 이미 익은 토마토 -> 이 토마토들은 모두 동시에 시작점
            queue.append((i, j)) # 익은 토마토를 시작점으로
            
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while queue:
    y, x = queue.popleft()
    
    for dy, dx in directions:
        ny = y + dy
        nx = x + dx
        
        if 0 <= ny < N and 0 <= nx < M: # 격자 안에서
            if box[ny][nx] ==0: # 익지 않은 토마토 발견
                box[ny][nx] = box[y][x] + 1 # 익히기
                queue.append((ny, nx)) # 날짜 기록
                
max_day = 0

for i in range(N):
    for j in range(M):
        if box[i][j] == 0: # 그래도 남아있는 0
            print(-1) # 못 익는 토마토 존재
            exit(0)
        max_day = max(max_day, box[i][j])
        
print(max_day - 1) # 처음 익은 토마토는 값이 1 -> 경과 일수는 1 빼야함