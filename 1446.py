# N과 D 입력
N, D = map(int, input().split())

road_list = [i for i in range(0, 10000)]
road_dict = {}

for i in range(0, N):
    start, end, length = map(int, input().split())
    road_dict[i] = [start, end, length]

for i in range(0, D+1):
    if i > 0:
        road_list[i] = min(road_list[i], road_list[i-1] + 1)
    for val in road_dict.values():
        if i == val[0] and val[1] <= D and road_list[i] + val[2] < road_list[val[1]]:
            road_list[val[1]] = road_list[i] + val[2]

print(road_list[D])