n, m = map(int, input().split())

for i in range(n):
    data = list(map(int, input().split()))
    data.sort()
    min = data[0]

print(min)