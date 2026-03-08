import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]

answer = 32

for x in range(N - 7):
    for y in range(M - 7):
        count_w = 0  # 왼쪽 위가 W
        count_b = 0  # 왼쪽 위가 B

        for i in range(8):
            for j in range(8):
                current = board[x + i][y + j]

                # 왼쪽 위가 W인 경우
                if (i + j) % 2 == 0:
                    if current != 'W':
                        count_w += 1
                    if current != 'B':
                        count_b += 1
                else:
                    if current != 'B':
                        count_w += 1
                    if current != 'W':
                        count_b += 1

        answer = min(answer, count_w, count_b)

print(answer)
