import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    
    field = [[0] * M for _ in range(N)]
    
    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1   # y가 행, x가 열
        
    visited = [[False] * M for _ in range(N)]
    
    def dfs(y, x):
        visited[y][x] = True # 이미 방문함
        
        # 상하좌우 탐색
        for dy, dx in [(1,0), (-1,0), (0,1), (0,-1)]: # 상하좌우 탐색
            ny = y + dy # 새로운 좌표 계산 
            nx = x + dx # 현재 위치에서 한칸 이동
            
            if 0 <= ny < N and 0 <= nx < M: # 격자 안에서 활동
                if field[ny][nx] == 1 and not visited[ny][nx]: # 배추가 있고, 아직 방문 안했으면
                    dfs(ny, nx) # 재귀 호출
    
    count = 0
    
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                count += 1
    
    print(count)