import sys
input = sys.stdin.readline

N = int(input())
A = set(map(int, input().split()))

M = int(input())
queries = list(map(int, input().split()))

for x in queries:
    if x in A :
        print(1)
    else : 
        print(0)