import sys
sys.setrecursionlimit(10**9)

N = int(input())

# 그래프의 연결을 포함하는 그래프 생성
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 그래프의 방문된 노드를 추적하는 세트
visited = set()
# 부모 코드 집어넣기
parent = [0 for _ in range(N+1)]

# DFS 함수
def dfs(node):
    # 조합에 방문한 노드를 집어넣는다.
    visited.add(node)        
    for neighbour in graph[node]:
        if neighbour not in visited:
            parent[neighbour] = node
            dfs(neighbour)

# 함수를 실행
dfs(1)
for i in range(2, N+1):
    print(parent[i])