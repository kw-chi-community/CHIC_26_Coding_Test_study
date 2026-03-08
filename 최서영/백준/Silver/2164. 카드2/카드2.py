from collections import deque

N = int(input())

cards = deque(range(1, N+1))

while len(cards) > 1:
    cards.popleft() # 맨 위 카드 버리기
    cards.append(cards.popleft()) # 다음 카드 맨 아래로
    
print(cards[0])