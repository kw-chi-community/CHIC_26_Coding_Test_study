import sys
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]

nums.sort()

# 산술평균
avg_raw = sum(nums) / N
if avg_raw >= 0:
    avg = int(avg_raw + 0.5)
else:
    avg = int(avg_raw - 0.5)

# 중앙값
median = nums[N // 2]

# 최빈값
from collections import Counter
count = Counter(nums)

max_freq = max(count.values()) #가장 많이 나온 횟수 찾기
modes = [num for num, freq in count.items() if freq == max_freq] # 최빈값 후보들을 전부 모은 리스트
modes.sort()

mode = modes[1] if len(modes) > 1 else modes[0]

# 범위
range_val = nums[-1] - nums[0]

print(avg)
print(median)
print(mode)
print(range_val)