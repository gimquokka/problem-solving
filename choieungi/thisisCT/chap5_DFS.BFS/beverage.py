#DFS_beverage
row, column = map(int, input().split())

#이차원 리스트 받기
ice_shape =[]
for i in range(row):
    ice_shape.append(list(map(int,input())))

def Dfs(x,y):
    #리스트 이탈 방지
    if x<0 or x>=row or y<0 or y>=column:
        return False  #이탈하면 강제 종료(num 할당 X)
    #방문 안한 노드
    if ice_shape[x][y]== False:
        ice_shape[x][y]= True #현 위치를 방문처리
        Dfs(x-1,y) #인접 노드로 이동
        Dfs(x,y-1)
        Dfs(x+1,y)
        Dfs(x,y+1)
        return True #방문 햇으므로 num 할당
    return False #모두 방문 했으면 강제 종료

#음료 얼음 개수
num =0
for i in range(row):
    for j in range(column):
        if Dfs(i,j) ==True:
            num+=1
print(num)
