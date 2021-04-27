# 왕실의 나이트
#print(chr(97)) a의 아스키코드 값은 97
#아스키 코드 가능 but 코드 복잡 

n= input()

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [-1, 1, -1, -1, 2, -2, 2, -2]

x_dict = {'a':1,'b':2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8}
x= x_dict[n[0]]
y=int(n[1])

count =0
for i in range(8) :
    nx = x + dx[i]
    ny = y + dy[i]
    if nx<1 or nx>8 or ny>8 or ny<1:
        continue
    count += 1

print(count)

