ans = []
num_of_input = int(input())
for _ in range(num_of_input):
    n, m = map(int, input().split())
    tmp = list(map(int, input().split()))

    data = []
    for i in range(n):
        data.append((tmp[i], i))

    count = 0
    while data:
        if (len(data) > 1) and (max(data[1:])[0] > data[0][0]):
            data.append(data.pop(0))
        else:
            now = data.pop(0)
            count += 1
            # now가 위의 else에 종속 됨으로 하위로 넣어주어야함.
            # 그렇지 않으면 항상 동작을 보장할 수 없음
            if now[1] == m:
                ans.append(count)
                break
for i in ans:
    print(i)
