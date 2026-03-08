import sys
input = sys.stdin.readline

N = int(input())
points = []

for _ in range(N):
    x, y = map(int, input().split())
    points.append((y, x)) # 순서를 바꿔서 저장
    
points.sort()

for y, x in points:
    print(x, y)