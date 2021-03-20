n = int(input())

data = list(map(int, input().split()))

add, sub, mul, div = map(int, input().split())

max_value = -int(1e9)
min_value = int(1e9)
cnt = 0


def dfs(i, now):
    global add, sub, mul, div, max_value, min_value

    if i == n:
        max_value = max(max_value, now)
        min_value = min(min_value, now)
    else:
        if add > 0:
            add -= 1
            dfs(i+1, now+data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, now-data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, now*data[i])
            mul += 1
        if div > 0:
            div -= 1
            # 이렇게 하면 굳이 if 안걸어도 됨.(0.이하 절사)
            dfs(i+1, int(now/data[i]))
            div += 1


dfs(1, data[0])

print(max_value)
print(min_value)
