import sys
input = sys.stdin.readline

M = int(input())
S = [False] * 21

for _ in range(M):
    command = input().split()

    if command[0] == "add":
        S[int(command[1])] = True

    elif command[0] == "remove":
        S[int(command[1])] = False

    elif command[0] == "check":
        print(1 if S[int(command[1])] else 0)

    elif command[0] == "toggle":
        x = int(command[1])
        S[x] = not S[x]

    elif command[0] == "all":
        S = [True] * 21

    elif command[0] == "empty":
        S = [False] * 21