from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    priorities = list(map(int, input().split()))
    
    # (중요도, 내가 찾는 문서인지)
    queue = deque()
    for i in range(N):
        queue.append((priorities[i], i == M))
    
    printed = 0
    
    while True:
        cur_priority, is_target = queue.popleft()
        
        # 뒤에 더 중요한 문서가 있는지
        if any(cur_priority < other[0] for other in queue):
            queue.append((cur_priority, is_target))
        else:
            printed += 1
            if is_target:
                print(printed)
                break