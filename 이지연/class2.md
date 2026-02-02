## 10989. 수 정렬하기 3

### 1차 시도
- 아이디어: 입력받은 모든 숫자를 리스트에 저장한 뒤 sort()사용하여 정렬.

```
import sys

n = int(sys.stdin.readline())
nums = []

for _ in range(n):
    nums.append(int(sys.stdin.readline()))

nums.sort()
for i in nums:
    print(i)
```
- 문제점 : 메모리 초과 발생

### 2차 시도

- 아이디어: 계수 정렬(Counting Sort) 원리를 활용하여 숫자를 직접 저장하지 않고, 각 숫자가 등장한 '횟수'만 기록함.

#### 핵심 원리: 
* 숫자의 범위가 10,000 이하이기에,  1부터 10,000까지의 인덱스를 가진 리스트를 미리 생성함. 
* 숫자를 입력받을 때마다 리스트에 담는 대신, 해당 인덱스의 값을 1씩 증가시킴.
* 마지막에 리스트를 순회하여 값이 1이상인 인덱스를 저장된 횟수만큼 출력.

```
import sys

n = int(sys.stdin.readline())
count = [0] * 10001

for _ in range(n):
    num = int(sys.stdin.readline())
    count[num] += 1

for i in range(1, 10001):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)
```

## 2869. 달팽이는 올라가고 싶다
### 1차 시도

- **아이디어**: 매일 낮에 올라가고 밤에 자는 과정을 그대로 반복문으로 구현

```
import sys

a,b,v = map(int, sys.stdin.readline().split())

height = 0
day = 0

while(height < v):
	day += 1
	height += a
	if height>= v :
		break
	height -= b

print(day)
```

효율성: 정상 높이(V)가 최대 10억이므로, 반복문으로 풀 경우 최악의 상황에서 10억 번의 연산이 필요함. -> 시간 초과 발생

### 2차 시도(해결)

- **아이디어**: 반복문 대신 수학 공식을 이용해 시간 복잡도를 $O(1)$로 단축.

- **핵심 원리**:달팽이가 정상에 도착하는 마지막 날은 밤에 미끄러지는 거리($B$)를 계산하지 않는다. 따라서 목표 지점을 $V$가 아닌, 마지막 날의 미끄러짐을 미리 제외한 $V - B$로 설정한다.하루에 실제로 올라가는 순수 거리인 $A - B$로 목표 지점을 나눈다. 이때 나머지가 발생하면 하루가 더 필요하다는 뜻이므로 '올림' 처리를 한다.

```
import sys
import math

a, b, v = map(int, sys.stdin.readline().split())
day = math.ceil((v - b) / (a - b))

print(day)
```

## 1920.수 찾기
1. 문제 분석 및 함정상황: N개의 숫자가 주어지고, M개의 숫자가 그 안에 존재하는지 확인해야 함.
2. 제한: N과 M은 최대 100,000, 시간 제한은 1초.함정
3. 선형 탐색의 한계:파이썬의 리스트에서 if num in list:를 사용하면 처음부터 끝까지 하나씩 확인하는 선형 탐색(O(N))을 수행함. M개의 숫자를 매번 리스트에서 찾으면 1초에 약 1억 번 연산이 가능한 파이썬에서는 무조건 시간 초과 발생.

### 해결 방법 1: 집합(Set) 활용 (O(N + M))
- 핵심 원리: 파이썬의 set은 Hash Table구조를 사용함.
- 장점: 특정 요소가 들어있는지 확인하는 탐색 복잡도가 평균 O(1).
- 결과: 리스트를 집합으로 변환하는 데 O(N), 탐색하는 데 O(M)이 걸려 전체적으로 아주 빠르게 해결 가능.
```
import sys

n = int(sys.stdin.readline())
n_set = set(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

for num in m_list:
    if num in n_set:
        print(1)
    else:
        print(0)
```

### 해결 방법 2: 이분 탐색(Binary Search) (O((N+M) log N))
핵심 원리: 데이터를 미리 정렬한 뒤, 탐색 범위를 매번 절반씩 좁혀나가며 값을 찾음.
장점: 탐색 복잡도가 O(log N)으로 리스트 탐색(O(N))보다 압도적으로 빠름.
조건: 반드시 데이터가 정렬된 상태여야 함.
```
import sys

def binary_search(target, array):
    start, end = 0, len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0

n = int(sys.stdin.readline())
n_list = sorted(list(map(int, sys.stdin.readline().split())))

m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

for num in m_list:
    print(binary_search(num, n_list)) 
```
## 11866.요세푸스 문제
### 방법1. 직접 회전(for문 + popleft + append)
- 로직: `k-1`번 반복하며 `popleft`한 값을 다시 `append`.
```
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
queue = deque(range(1, n + 1))
result = []

while queue:
    # 1. k-1번만큼 앞에서 꺼내서 뒤로 보내기
    for _ in range(k - 1):
        moved_person = queue.popleft() 
        queue.append(moved_person)     
    
    # 2. k번째 사람을 제거하여 결과에 추가
    result.append(queue.popleft())

print("<" + ", ".join(map(str, result)) + ">")
```

### 방법2. rotate함수 활용하기
- 특징: 파이썬 `deque` 모듈의 내부 최적화된 기능을 사용함.
- 로직: `queue.rotate(-(k-1))` 한 줄로 `k-1`명을 뒤로 보냄.
- 주의: `rotate(-1)`은 왼쪽 회전(앞→뒤), `rotate(1)`은 오른쪽 회전(뒤→앞)임.
```
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
queue = deque(range(1, n + 1))
result = []

while queue:
    # 1. 왼쪽으로 (k-1)칸 회전 (음수면 앞의 것이 뒤로 이동)
    queue.rotate(-(k - 1))
    
    # 2. k번째 사람을 제거하여 결과에 추가
    result.append(queue.popleft())

print("<" + ", ".join(map(str, result)) + ">")
```

## 11651.좌표 정렬하기2
- 핵심 개념: 정렬 기준 커스텀 (`key=lambda`)
- 사용법: `리스트.sort(key=lambda x: (기준1, 기준2))`
  - `points.sort(key=lambda x: (x[1], x[0]))`   
  - `x[1]`은 $y$좌표를, `x[0]`은 $x$좌표를 의미한다.
  - 괄호 `()` 안에 적은 순서대로 정렬 우선순위가 결정된다.
- **응용**:
  - 내림차순이 필요하면 마이너스(`-`)를 붙인다: `key=lambda x: (x[1], -x[0])` 
    -> $y$는 오름차순, $x$는 내림차순 정렬
