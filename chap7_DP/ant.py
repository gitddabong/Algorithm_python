n = int(input())
array = list(map(int, input().split()))
data = [0] * 100        # 어느 선택이 가장 이득인지 저장하는 테이블

data[0] = array[0]
data[1] = max(array[0], array[1])
for i in range(2, n):
    data[i] = max(data(i-2) + array[i], data(i-1))

print(data(n-1))    # n이라고 쓰면 오버플로우
