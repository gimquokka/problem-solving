def num_conditions(x,y,a, result): # 세울 수 있게 만드는 조건 수
    
    count = 0
    if a == 0: # 기둥일때 존재 조건 수 세기
        if y == 0: # 바닥
            count += 1
        if [x-1,y,1] in result:
         # 왼쪽 보 위에 
            count +=1
        if [x,y-1,0] in result:
         # 다른 기둥 위에 
            count += 1
        if [x,y,1] in result:
         # 같은 교차점에 있는 보 위에
            count += 1
        
    if a == 1: # 보일때
        if [x,y-1,0] in result:
        #  끝부분이 기둥 위에 1
            count += 1
        if [x+1,y-1,0] in result:
         #  끝부분이 기둥 위에 1
            count += 1
        if [x-1,y,1] in result and [x+1,y,1] in result:
        # 양쪽 끝부분이 다른 보와 동시에 연결
            count += 1
    return count

def solution(build_frame):
    n = len(build_frame)
    result = []
    
    
    
    
    # 인덱스 확인하기..! outofrange!
    for arr in build_frame:  # arr = [1,0,0,1] , ..
        
        x,y,a,b = arr
        if b == 1: # 설치
            if num_conditions(x,y,a, result) >=1:  # 바닥 or 보 한쪽 끝부분 위에  or 다른 기둥 위에
                
                result.append([x,y,a])
                
                    
            
        if b == 0: # 삭제
            if a == 0: #기둥삭제
                
                # 기둥에 영향 받는 것들 중에 조건이 1개라면 기동이 삭제되면 안됨
                if num_conditions(x,y+1,0,result) == 1 or num_conditions(x-1,y+1,1,result) == 1 or num_conditions(x,y+1,1,result) == 1: 
            
                    continue 


            else: # 보 삭제
                if num_conditions(x-1,y,1,result) == 1 or num_conditions(x+1,y,1,result) == 1 or num_conditions(x,y,0,result) == 1 or num_conditions(x+1,y,0,result) == 1:
                    continue
            
            result.remove([x,y,a])

    for i in range(2,-1, -1): #lexicographic sorting
        result.sort(key = lambda x: x[i])
    
    return result

build_frame1 = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
build_frame2 = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

print(solution(build_frame2))


# 기둥설치 : 교차점이 바닥 -> 설치 , 바닥 아닌데 교차점 왼쪽에 보 있거나 아래에 기둥있거나 교차점에 보 있으면 설치
# 보 설치 : 교차점 아래나 교차점 오른쪽 아래에 기둥 있으면, 아니면 왼쪽에 or 오른쪽에 보 


# 버티는 조건이 되는 튜플 만들기 : 
# 기둥 삭제: 교차점 위만.. 교차점 위 기둥, 위 왼쪽 보 , 위 보 영향
# 보 삭제 : 교차점에서 왼쪽보, 오른쪽보, 교차점 기둥, 교차점 오른쪽 기둥 영향