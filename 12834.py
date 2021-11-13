import heapq

# 첫쨰줄
n, v, e = map(int, input().split())

# 둘째줄
destination = list(map(int, input().split()))

# 셋째줄
team_mate = list(map(int, input().split()))

# 넷째줄
graph = [[] for _ in range(v+1)]

# 시작, 끝, 가중치 입력받기
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# 다익스트라 함수
def dijkstra(start, distance):
    # 시작 노드의 거리는 0으로 설정
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (distance[start], start))
    
    while queue:
        dist, node = heapq.heappop(queue)

        if distance[node] < dist:
            continue

        for next in graph[node]:
            weighted_distance = dist + next[1]
            if weighted_distance < distance[next[0]]:
                distance[next[0]] = weighted_distance
                heapq.heappush(queue, (weighted_distance, next[0]))

total_dis = 0

for i in range(n):
    KIST = 0
    FOOD = 0
    # 장소 기억해야되는데 팀원 수마다 새로 설정해줘야 함
    INF = 10001
    distances = [INF] * (v+1)
    dijkstra(team_mate[i], distances)
    if distances[destination[0]] == INF:
        KIST = -1
    if distances[destination[1]] == INF:
        FOOD = -1
    if distances[destination[0]] != INF:
        KIST = distances[destination[0]]
    if distances[destination[1]] != INF:
        FOOD = distances[destination[1]]
    
    total_dis = total_dis + KIST + FOOD

print(total_dis)
