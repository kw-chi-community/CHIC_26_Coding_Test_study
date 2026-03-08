import sys
input = sys.stdin.readline

n = int(input())
sequence = [int(input()) for _ in range(n)]

stack = []
result = []
cur = 1

for num in sequence:
    while cur <= num:
        stack.append(cur)
        result.append('+')
        cur += 1
        
    if stack and stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        print("NO")
        sys.exit()
        
print('\n'.join(result))