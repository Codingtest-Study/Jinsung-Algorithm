# 서버실 크기
N = int(input())

# 각 칸의 컴퓨터
computer = []
total_computers = 0
max_value = 0

# 입력받기
for _ in range(N):
    number = list(map(int, input().split()))
    computer.append(number)
    max_value = max(max_value, max(number))
    total_computers += sum(number)

# 냉동의 높이
level = 0

# 이진 탐색 시작
first, last = 0, max_value
while first <= last:
    mid = (first + last) // 2
    total_value = 0
    for i in range(N):
        for j in range(N):
            total_value += (mid if mid <= computer[i][j] else computer[i][j])
    
    if total_value >= total_computers/2:
        level = mid
        last = mid - 1
    else:
        first = mid + 1

print(level)