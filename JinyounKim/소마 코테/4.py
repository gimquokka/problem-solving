def main():
    n = int(input())
    data = list(map(int, input().split()))
    ans = []
    for i in range(1):
        visited = [False]*n
        cnt = 1
        now = i
        visited[now] = True
        for j in range(n):
            now += data[now]
            if visited[now]:
                cnt +=1
                break
            visited[now] = True
            cnt += 1
            # print(now)
        ans.append(cnt)

    print(max(ans))


if __name__ == "__main__":
    main()
