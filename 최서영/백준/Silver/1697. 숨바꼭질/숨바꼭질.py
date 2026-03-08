from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

MAX = 100001
visited = [False] * MAX

queue = deque()
queue.append((N, 0)) # 현재 위치, 걸린 시간
visited[N] = True # 이미 방문

while queue:
    position, time = queue.popleft() # 가장 먼저 들어온 위치 꺼냄
    
    if position == K: 
        print(time)
        break
    
    for next_pos in (position - 1, position + 1, position * 2): # 현재 위치 X에서 갈 수 있는 곳
        if 0 <= next_pos < MAX and not visited[next_pos]: # 범위 체크
            visited[next_pos] = True
            queue.append((next_pos, time + 1)) # 다음 위치, 시간은 1초 증가