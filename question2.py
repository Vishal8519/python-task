import math

N = int(input())

count = 0
for start in range(1, int(math.sqrt(N)) + 1):
    if start % 2 == 0:
        continue
    total = (N - start + 1) * (start + N) // 2
    if total % N == 0 and total % 2 != 0:
        count += 1

print(count)

