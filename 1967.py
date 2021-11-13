# visited는 방문여부 확인
# start는 DFS에서 시작 위치
# prev_len은 지금까지의 길이
# max_len은 최대 길이를 저장하는 현재 노드
def DFS(graph, start, prev_len, max_len, visited):
    # 방문했을 경우 1로 설정
    visited[start] = 1

    # 현재 길이는 케이블의 길이
    curr_len = 0

    # 2개의 인접한 노드
    adjacent = None

    for i in range(len(graph[start])):
        adjacent = graph[start][i]

        if not visited[adjacent[0]]:
            curr_len = prev_len + adjacent[1]

            DFS(graph, adjacent[0], curr_len, max_len, visited)

        if max_len[0] < curr_len:
            max_len[0] = curr_len
        
        # 초기화
        curr_len = 0

# n은 그래프에서 노드의 개수
def longestPath(graph, n):
    # 최장 갈이
    max_len = [-9999999]

    # DFS 호출
    for i in range(1, n+1):
        visited = [False] * (n+1)
        DFS(graph, i, 0, max_len, visited)

    return max_len[0]

# DFS는 시간초과 발생 =====================================================

from collections import deque

class Graph:

    # vertices는 노드의 수
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj = [[] for _ in range(self.vertices)]
    
    # 연결점과 가중치를 더한 것을 adj라는 곳에 선언
    def addEdge(self, u, v, w):
        self.adj[u].append([v, w])
        self.adj[v].append([u, w])
    
    def BFS(self, u, mode):
        distance = [-1 for _ in range(self.vertices + 1)]

        distance[u] = 0
        queue = deque()
        queue.append(u)

        while queue:

            first = queue.popleft()

            for node, weight in self.adj[first]:
                if distance[node] == -1:
                    distance[node] = distance[first] + weight
                    queue.append(node)
        
        if mode == 1:
            return distance.index(max(distance))
        else:
            return max(distance)

# 노드의 개수 입력
number_of_node = int(input())

G = Graph(number_of_node)

# 노드의 개수 - 1 만큼 [부모, 자식, 가중치] 입력
for _ in range(number_of_node-1):
    parent, child, weight = map(int, input().split())
    G.addEdge(parent-1, child-1, weight)

print(G.BFS(G.BFS(0, 1), 2))