n = int(input())
cnt = 0
list_for =[]

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                cnt += 1
                list_for.append([i, j, k])

print(cnt)


list_while = []

hour = 0
min = 0
sec = 0
cnt = 0

while True:
    if n == hour + 1:
        break

    if sec == 60:
        sec = 0
        min += 1

    if min == 60:
        min = 0
        hour += 1

    if '3' in str(hour) + str(min) + str(sec):
        cnt += 1
        list_while.append([hour, min, sec])

    sec += 1

print(cnt)


index = 0

for i in range(cnt):
    if list_for[i] == list_while[index]:
        index += 1
    else:
        print(list_for[i])
    