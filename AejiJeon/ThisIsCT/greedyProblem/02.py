lst = list(map(int, input()))

result = lst[0]
# 02984  1948038
for i in range(1, len(lst)):
    num = lst[i]
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
