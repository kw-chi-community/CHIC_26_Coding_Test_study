# 회의를 끝나는 시간 기준으로 오름차순 정렬
# 하나 선택
# 그 다음 시작 시간이 이전 끝 시간 이상인 것만 선택

import sys
input = sys.stdin.readline

N = int(input())

meetings = []
for _ in range(N):
    start, end = map(int, input().split())
    meetings.append((start, end))    

# 끝나는 시간 기준 정렬
meetings.sort(key=lambda x: (x[1], x[0])) # (회의 끝나는 시간, 회의 시작 시간)

count = 0
current_end = 0

for start, end in meetings:
    if start >= current_end: # 그 다음 시작 시간이 이전 끝 시간 이상인 것만 선택
        count += 1
        current_end = end
        
print(count)