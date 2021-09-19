n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m+1)
d[0] = 0

for i in array:     # 화폐 단위 모음
    for j in range(i, m+1):
        if(j - i) != 10001:
            d[j] = min(d[j], d[j - i] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])