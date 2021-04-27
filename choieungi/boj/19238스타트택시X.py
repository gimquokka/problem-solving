from collections import deque
import copy
n,m, fuel = map(int,input().split())

space=[]
for _ in range(n):
    space.append(list(map(int,input().split())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

x,y= map(int,input().split())
x-=1
y-=1

customer =[]
destination =[]

#print(space)
#print(customer,destination)

def bfs(x,y,fx,fy,spaces):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+ dx[i]
            ny = y+ dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<n:
                if spaces[nx][ny] == 1:
                    continue
                if spaces[nx][ny] ==0:
                    spaces[nx][ny] = spaces[x][y]+1
                    queue.append((nx,ny))

    return (spaces[fx][fy], (fx,fy))

#목적지 성공하면 승객을 태워 가는데 걸린 연료의 두배 만큼 더한다

to_go =[]
for _ in range(m):
    a,b,c,d = map(int,input().split())
    to_go.append((a-1,b-1,c-1,d-1))

while to_go:
    vir_space = copy.deepcopy(space)
    customer_used_fuel = []
    #print('x,y,m:',x,y,m)
    #최단 거리 찾기
    for i in to_go:
        cx,cy = i[0] ,i[1]
        #print(bfs(x,y,cx,cy,space))
        customer_used_fuel.append(bfs(x,y,cx,cy,vir_space))
    vir_space = copy.deepcopy(space)
    customer_used_fuel.sort(key=lambda x:(x[0],x[1][0],x[1][1]))
    #print(customer_used_fuel)
    used_fuel=customer_used_fuel[0][0]
    p, q = customer_used_fuel[0][1]
    #print(customer_used_fuel)
    #print(p,q,to_go,end=' ')
    if used_fuel > fuel:
        fuel = -1
        print(-1)
        break
    elif used_fuel ==0 and (cx-x !=0 or cy-y!=0) :
        fuel = -1
        print(fuel)
        break
    else:
        fuel -= used_fuel
    #print(fuel)
    #print(fuel)
    #승객을 태우고 최단 경로 구하기
    for a,b,c,d in to_go:
            if a==p and b== q :
                temp =bfs(p,q,c,d,vir_space)
                #print('값:',temp)
                used_fuel,location= temp
                to_go.remove((a,b,c,d))

    if used_fuel > fuel:
        fuel=-1
        print(-1)
        break
    elif used_fuel ==0:
        fuel = -1
        print(fuel)
        break
    else:
        fuel += used_fuel
    x,y = location
    m-=1

if fuel !=-1 :
    print(fuel)


 #   p,q = customer_used_fuel[0][1][1]
  #  destination_used_fuel.append(p,)



'''
    if used_fuel > fuel:
        print(-1)
    else:
        fuel -= used_fuel
    print(fuel)

    used_fuel = bfs(a-1,b-1,c-1,d-1,space,fuel)

    if used_fuel > fuel:
        print(-1)
    else:
        fuel += used_fuel

    print(fuel)
'''

