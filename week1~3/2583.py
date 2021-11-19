from collections import deque

# m, n, k를 입력 받음
# m은 y좌표 n은 x 좌표
m, n, k = map(int, input().split())

# m과 n으로 이루어진 2차 행렬 선언
m_n_list = [[0 for _ in range(n)] for _ in range(m)]

# 0 2 4 4 이면 (0, 2)와 (4, 4)로 이루어진 직사각형에는 못들어감
# 2차 배열 리스트에서 x는 0, 1, 2, 3, y는 2, 3인 조합에는 미리 방문한 곳이라고 체크함
for _ in range(k):
    x0, y0, x1, y1 = map(int, input().split())
    for i in range(y0, y1):
        for j in range(x0, x1):
            if m_n_list[i][j] == 0:
                m_n_list[i][j] = 1

# 넓이 저장 배열 선언
width = []

# bfs 선언
def bfs(x, y):
    # 상하좌우에 필요한 좌표
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]

    # 초기 넓이 선언
    initial_width = 0

    # 큐 선언
    q = []

    # 초기 좌표 삽입
    q.append((x, y))

    # 초기 좌표 방문한 것으로 바꾸고 넓이 더함
    m_n_list[y][x] = 1
    initial_width += 1

    while q:
        x_, y_ = q.pop(0)

        for i in range(4):
            new_x_ = x_ + dx[i]
            new_y_ = y_ + dy[i]
            if 0 <= new_x_ < n and 0 <= new_y_ < m and m_n_list[new_y_][new_x_] == 0:
                m_n_list[new_y_][new_x_] = 1
                initial_width += 1
                q.append((new_x_, new_y_))
    
    return initial_width

# 모든 좌표를 확인하며 필요한 것만 bfs 실행
for i in range(m):
    for j in range(n):
        if m_n_list[i][j] == 0 and 0 <= j < n and 0 <= i < m:
            width.append(bfs(j, i))

# 오름차순으로 정렬하고 출력하기
width.sort()
print(len(width))
print(*width)
            