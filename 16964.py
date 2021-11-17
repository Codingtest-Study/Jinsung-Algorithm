# 정점의 수 입력 받음
N = int(input())

# 그래프의 연결을 포함하는 그래프 생성
graph = [[] for i in range(N+1)]

for _ in range(N-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 그래프의 방문된 노드를 추적하는 세트
visit_set = []

# DFS 함수
def dfs(node):
    # 조합에 방문한 노드를 집어넣는다.
    visit_set.append(node)        
    for neighbour in graph[node]:
        if neighbour not in visit_set:
            dfs(neighbour)

# 확인해야하는 DFS 알고리즘
check_dfs = list(map(int, input().split()))

# 방문 순서
order = [0] * (N+1)

if check_dfs[0] != 1:
    print(0)
else:
    # 방문 순서를 각각 저장
    for i in range(1, N+1):
        order[check_dfs[i-1]] = i
    
    # 방문 순서대로 그래프 정렬
    for i in range(1, N+1):
        graph[i] = sorted(graph[i], key=lambda j : order[j])
    
    dfs(1)

    if visit_set == check_dfs:
        print(1)
    else:
        print(0)