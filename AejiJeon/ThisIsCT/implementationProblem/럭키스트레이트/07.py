lst = list(map(int, input()))  # [1,2,3,4,0,2] l = 6 l/2 = 3 [7,7,5,5]  l = 4 l/2 = 2

l = len(lst)
left_lst = lst[:l//2]
right_lst = lst[l//2:]

if sum(left_lst) == sum(right_lst):
    print("LUCKY")
else:
    print("READY")


