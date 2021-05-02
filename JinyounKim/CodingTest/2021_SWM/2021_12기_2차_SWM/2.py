def main():
    n = int(input())
    data = list(map(int, input().split()))
    ans = 0
    for i in range(1):
        path = []
        now = i
        for _ in range(2*n):
            step = data[now]
            now += step
            path.append(step)
        for start in range(n):
            for end in range(start+1, n):
                if sum(path[start: end]) == 0:
                    ans = max(ans, len(path[start: end]))
    print(ans)


if __name__ == "__main__":
    main()
