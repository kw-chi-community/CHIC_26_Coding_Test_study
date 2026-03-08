import sys
input = sys.stdin.readline

N = int(input())
points = []

for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

points.sort() # (x, y) 튜플은 리스트에 넣고 그냥 정렬하면 x->y순으로 자동 정렬

for x, y in points:
    print(x, y)