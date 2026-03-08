import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

# 각 컴퓨터가 연결된 목록 저장 (인접 리스트)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) # 둘다 필요한 이유 : 무방향 그래프 -> 양쪽에 모두 추가

# visited(방문 배열) : 중복 방문 방지, 무한 루프 방지
visited = [False] * (N + 1) # visited[i] = True : i번 컴퓨터는 이미 방문

# dfs 함수 : 현재 노드 방문 표시, 연결된 노드 재귀 탐색, 방문 개수 누적
def dfs(node):
    visited[node] = True # 이미 방문했기 때문에 count = 1
    count = 1
    
    for next_node in graph[node]:
        if not visited[next_node]: # 아직 감염되지 않았으면 
            count += dfs(next_node) # 연결된 컴퓨터로 재귀 탐색, 그 컴퓨터에서 감염된 수를 더함
    
    return count

# 1번에서 시작
result = dfs(1)

# 1번 자신 제외
print(result - 1)