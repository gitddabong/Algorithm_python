n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

max1 = data[n - 1]
max2 = data[n - 2]
cnt = 0
result = 0

for i in range(m):
    if cnt < 3:
        result = result + max1
        cnt += 1
    else:
        result = result + max2
        cnt = 0

print(result)