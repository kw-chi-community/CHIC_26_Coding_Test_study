N = int(input())
people = []

for _ in range(N):
    w, h = map(int, input().split())
    people.append((w, h))

ranks = []

for i in range(N):
    rank = 1
    for j in range(N):
        if people[j][0] > people[i][0] and people[j][1] > people[i][1]:
            rank += 1 # 내 등수만 하나 밀림 이슈
    ranks.append(rank)
    
print(*ranks) # 리스트에 들어있는 값들을 하나씩 꺼내서 공백으로 출력하라