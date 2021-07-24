n, m = map(int, input().split())

row, column, look = map(int, input().split())

array = []
for i in range(n):
    array.append(list(map(int, input().split())))
    
cnt = 1         # 방문한 칸
turn_cnt = 0    # 회전 횟수

while True:
    turn_cnt = 0
    # 회전
    for i in range(4):
        if look == 0:
            if array[row][column-1] == 0:     # 서쪽으로 한 칸 이동이 가능한 경우
                look = (look - 1) % 4
                array[row][column] = 1
                column -= 1
                cnt += 1
                break
            else:           # 이동이 불가능하면 회전
                look = (look - 1) % 4
                turn_cnt += 1
                continue

        if look == 3:
            if array[row+1][column] == 0:       # 남쪽으로 한 칸 이동이 가능한 경우
                look = (look - 1) % 4
                array[row][column] = 1
                row += 1
                cnt += 1
                break
            else:
                look = (look - 1) % 4
                turn_cnt += 1
                continue
  
        if look == 2:
            if array[row][column+1] == 0:     # 동쪽으로 한 칸 이동이 가능한 경우
                look = (look - 1) % 4
                array[row][column] = 1
                column += 1
                cnt += 1
                break
            else:           # 이동이 불가능하면 회전
                look = (look - 1) % 4
                turn_cnt += 1
                continue

        if look == 1:
            if array[row-1][column] == 0:       # 북쪽으로 한 칸 이동이 가능한 경우
                look = (look - 1) % 4
                array[row][column] = 1
                row -= 1
                cnt += 1
                break
            else:
                look = (look - 1) % 4
                turn_cnt += 1
                continue

    if turn_cnt == 4:
        break

print(cnt)