arr = [input().strip() for _ in range(3)]

start = 0

# 숫자 문자열을 찾아서 시작 숫자 추정
for idx in range(3):
    if arr[idx].isdigit():
        start = int(arr[idx]) - idx
        break
        
# 다음 숫자 (i+3)
nxt = start + 3

# 규칙 사용
if nxt % 15 == 0:
    print("FizzBuzz")
elif nxt % 3 == 0:
    print("Fizz")
elif nxt % 5 == 0:
    print("Buzz")
else:
    print(nxt)