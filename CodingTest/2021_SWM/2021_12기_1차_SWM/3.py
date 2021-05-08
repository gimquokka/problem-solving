def main():
    n, m, now = map(int, input().split())
    data = list(map(int, input().split()))
    ans = []
    for i in range(n-m):
        if (data[i] > now):
            ans.append(abs(data[i+m-1] - now))
        elif data[i+m-1] < now:
            ans.append(abs(data[i] - now))
        else:
            ans.append(abs(data[i]-now) + abs(data[i+m-1]-now))
    
    print(min(ans))

if __name__=="__main__":
    main()