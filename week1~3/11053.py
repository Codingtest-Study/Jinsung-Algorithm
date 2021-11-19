n = int(input())
n_list = list(map(int, input().split( )))
store_list = [0] * n

for i in range(0, n):
    if i == 0:
        store_list[i] = 1
    else:
        max_value = 0
        for j in range(0, i):
            if max_value < store_list[j] and n_list[j] < n_list[i]:
                max_value = store_list[j]
        store_list[i] = max_value + 1

print(max(store_list))