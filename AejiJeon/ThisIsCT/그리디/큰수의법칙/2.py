n, m, k = map(int, input().split())

lst = list(map(int, input().split()))

lst = sorted(lst)

first = lst[n-1]
second = lst[n-2]


count = (m//(k+1))*k + m%(k+1)

result = 0
result += first * count
result += second * (m-count)



print(result)





