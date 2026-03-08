import sys
input = sys.stdin.readline

N = int(input())
members = []

for _ in range(N):
    age, name = input().split()
    members.append((int(age), name))
    
members.sort(key=lambda x: x[0]) # 나이순으로 정렬
# 나이가 같으면 자동으로 입력 순서 유지

for age, name in members:
    print(age, name)