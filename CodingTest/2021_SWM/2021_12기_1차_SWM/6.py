def main():
    n = int(input())
    data = list(map(int, input().split()))
    s = 0
    e = n
    ans = 0
    while s != e-1:
        m = (s+e)//2
        if max(data[s:m]) > max(data[m:e]):
            ans += max(data[s:m])
            s = m
        else:
            ans += max(data[m:e])
            e = m
        # print(m, ans)
    print(ans)


if __name__ == "__main__":
    main()
