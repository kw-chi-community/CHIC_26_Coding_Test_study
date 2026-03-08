import sys
input = sys.stdin.readline

N = int(input())
nums = []

for _ in range(N):
    nums.append(int(input()))

nums.sort()

out = sys.stdout.write
for x in nums:
    out(str(x) + '\n')