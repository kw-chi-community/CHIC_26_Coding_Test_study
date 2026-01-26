### 문자 -> 아스키 코드(정수) 변환
```
ch = input()
print(ord(ch))
```

### 입력된 Ndl chleo 1,000,000으로 입력이 클때
```
import sys

input = sys.stdin.readline
```

### split()의 특징
```
"Hello World ".split()
# 결과 -> ["Hello,", "World"]
```

### find()의 특징
```
S.find('a')
```
문자가 있으면 -> 처음 등장한 인덱스
없으면 -> -1

### ord() : 문자 -> 숫자
ord(문자) -> 숫자
```
ord('a')  # 97
ord('b')  # 98
ord('z')  # 122

ord('A')  # 65
ord('0')  # 48
```

### chr() : 숫자 -> 문자
chr(정수) -> 문자
```
chr(97)   # 'a'
chr(98)   # 'b'
chr(122)  # 'z'

chr(65)   # 'A'
chr(48)   # '0'
```