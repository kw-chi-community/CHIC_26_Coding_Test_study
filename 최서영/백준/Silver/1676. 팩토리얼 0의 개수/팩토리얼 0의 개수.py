# factorial 안에 (2x5)쌍이 몇개가 있는지 찾기 -> 직접 factorial 구함 X
# 2는 짝수마다 포함됨
# 5는 5의 배수에서만 등장
# 0의 개수 = 5의 개수

N = int(input())

count = 0
div = 5

while div <= N : 
    count += N // div
    div *= 5
    
print(count)