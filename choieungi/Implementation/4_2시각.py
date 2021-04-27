# 시각
# 3이 포함 되면 카운트

n= int(input(''))
count = 0
for i in range(n+1):
    for j in range(60):
        for w in range(60):
            a=("%02d%02d%02d"%(i,j,w))
            if '3' in a:
                count +=1

print(count)

# %d로 정수를 받으면 문자형으로 변경된다.



