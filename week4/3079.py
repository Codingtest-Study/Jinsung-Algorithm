# 심사대와 승객 입력 받음
N, M = map(int, input().split())

# 심사대 걸리는 시간을 순서대로 집어넣음
Tk = []
for _ in range(N):
    time = int(input())
    Tk.append(time)

# 효율이 제일 안좋은 최댓값
max_value = max(Tk) * M
low_value = min(Tk)

# 이진 탐색 진행
while low_value < max_value:
    # 효율의 중간 값을 찾고
    mid_value = (low_value + max_value) // 2

    # 통과하는 승객 수
    require_value = 0
    
    # 통과하는 승객 수 = 주어진 시간 // 심사대 시간
    for i in range(N):
        require_value += mid_value // Tk[i]
    
    if require_value < M:
        low_value = mid_value + 1
    else:
        max_value = mid_value

print(max_value)