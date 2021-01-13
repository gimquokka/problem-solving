# month -> season

a = input()

a = int(a)

if a in [12, 1, 2]:
    print("winter")
elif a in [3, 4, 5]:
    print("spring")
elif a in [6, 7, 8]:
    print("summer")
elif a in [9, 10, 11]:
    print("fall")