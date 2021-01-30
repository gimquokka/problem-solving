from itertools import combinations  

n = int(input())

# 입력받은 복도
graph = []
# 선생님들 위치를 담음
lst_Ts = []
# 빈 곳 위치를 담음
lst_Xs = []

for i in range(n):
    data = input().split()
    graph.append(data)
    for j in range(n):
        if data[j] == 'T':
            lst_Ts.append((i,j))
        elif data[j] == 'X':
            lst_Xs.append((i,j))


# (x,y) 위치에서 상 하 좌 우 확인
def check_cross(x, y):
    # 변화량 값
    da = [0,0,1,-1]
    db = [1,-1,0,0]
    for i in range(4):
        
        a,b = x,y

        while True:

            # 한칸 이동 후 위치
            na = a + da[i]
            nb = b + db[i]
            # 복도 밖
            if na < 0 or na > n-1 or nb < 0 or nb > n-1:
                break
            # 장애물 발견
            elif graph[na][nb] == 'O' :
                break
            # 빈칸 -> 그 다음 칸 확인
            elif graph[na][nb] == 'X':
                a,b = na, nb
            # 학생 발견
            elif graph[na][nb] == 'S':
                return False
    # 상 하 좌 우 학생 안 보임
    return True

def possible():
    # 빈 곳에 장애물 3개 놓는 모든 조합, comb: 위치 3개 들어있는 tuple 
    for comb in combinations(lst_Xs, 3):

        checking = True
        # 장애물 설치
        for x,y in comb:
            graph[x][y] = 'O'
        
        # 선생님들 감시 진행        
        for x, y in lst_Ts:
            # 중간에 학생 발견
            if not check_cross(x,y):
                checking = False
                break
        # 모든 선생님 감시 진행 후 -> 중간에 학생 발견하지 않음(True 유지)
        if checking:
            return True
        # 감시 피하기 실패 -> 장애물 설치 되돌리기 
        for x,y in comb:
            graph[x][y] = 'X'

    return False


print("YES" if possible() else "NO")
