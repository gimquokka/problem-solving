#작은 것부터 빼면서 0이 되고 안되고를 통해 완성
# 이중 반복문에서 두번째 반복문에서 continue하면 첫번 째 반복문으로 돌아감.

n = int(input())
num = list(map(int,input().split()))
num.sort() #내림차순 정렬 for greedy algorithm
result = 0


for i in range(1,sum(num)):
    temp = i
    for j in num:
        temp = temp-j
        if temp-j >0:
            pass
        elif temp-j==0:
            continue
        else:
            result=i
            break

if result==0:
    result = sum(num)+1
    print(result)
else:
    print(result)
