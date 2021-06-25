n, m, k = map(int, input().split())
arr = sorted(map(int, input().split()), reverse=True)
print(type(arr))

cnt, remain =divmod(m, k+1)

print((cnt*k+remain)*arr[0]+cnt*arr[1])