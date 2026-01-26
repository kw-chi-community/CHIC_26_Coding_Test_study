### 소수 구하기
1. 1은 소수 아님
2. 소수 판별 방법
    - 2부터 √x까지 나누어 봄 
    - 하나라도 나누어 떨어지면 X, 끝까지 안나누어지면 O 
    -  2부터 √x까지만 보는 이유 : √x보다 큰 약수는 이미 앞에서 짝이 다 나왔기 때문
```
N = int(input())
nums = list(map(int, input().split()))

count = 0

for x in nums:
    if x < 2:
        continue
    
    is_prime = True // 지금 이 숫자가 소수일 가능성이 아직 남아있는지를 기억하는 변수
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            is_prime = False
            break
            
    if is_prime:
        count += 1
        
print(count)
```

### 한자리씩 더해주는 방법
파이썬에서는 문자열로 바꿔줌 -> sum(map(int, str(x)))

### 최대공약수(GCD) & 최소공배수(LCM)
GCD(a, b) X LCM(a, b) = a X b
LCM(a, b) = (a X b) / GCD(a, b)
```
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

g = gcd(A, B)
l = A * B // g
```

### lambda x
def 함수에서 return을 생략하고 사용할 수 있는 함수

기본 구조
```
lambda 매개변수들 : 반환값
```

### print(*ranks)
: 리스트에 들어있는 값들을 하나씩 꺼내서 공백으로 출력하라는 의미
```
for i in range(len(ranks)):
    print(ranks[i], end=' ')
```
ranks = [2, 2, 1, 2, 5]
print(ranks)
를 실행하면 [2, 2, 1, 2, 5] 가 나오게 됨

print(*ranks)를 실행하면 
1. 리스트를 풀어서
2. print에 여러 개의 인자로 전달
-> 기본 구분자(공백)로 출력됨

### (x, y) 튜플은 리스트에 넣고 그냥 정렬하면 x->y순으로 자동 정렬

### set과 리스트
1. 리스트 : 앞에서부터 하나씩 비교
2. set : 해시(hash)로 바로 의치 확인 -> 있는지 없는지만 볼 땐 set이 최강 좋음

### 파이썬에서는 반올림 할 때 round()를 사용하지 않음
1. 반올림 -> int(x + 0.5) 
2. 소수점 버림 -> int(x)
3. 올림 -> math.ceil()
4. 내림 -> math.floor()

