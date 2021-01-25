# sol1
n, m = map(int, input().split())
lst = list(map(int, input().split()))
count_l = [0 for _ in range(m+1)]

for i in lst:
    count_l[i] += 1

no_dup_lst = list(set(lst))
no_dup_lst.sort()
l = len(no_dup_lst)
count = 0
for i in range(l-1):
    for j in range(i+1, l):
        count += count_l[no_dup_lst[i]]*count_l[no_dup_lst[j]]

print(count)

# sol2

# n, m = map(int, input().split())
# lst = list(map(int, input().split()))

# count = 0

# for i in range(n-1):
#     for j in range(i+1, n):
#         if lst[i] != lst[j]:
#             count += 1

# print(count)