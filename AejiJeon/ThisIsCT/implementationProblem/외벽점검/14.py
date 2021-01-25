
def solution(n, week, dist):
    num_people = len(dist)
    num_week = len(week)
    dist.reverse() # [4,3,2,1]


    for i in range(1, num_people+1): #1명부터~ 늘려가기  

        group = []  # 조사하러 나가는 사람들   [4,3]
        
        for j in range(i):  
            group.append(dist[j])
        
        
        for start in week:   # [1,5,6,10] 
            compared = []
             
            for p in group: # 4, 3
                
                for k in list(range(start,start+p+1)):
                    k %= n
                    if k in week:
                        compared.append(k)
                        
                start = week[(week.index(compared[-1]) + 1)%num_week]
            
            if week == sorted(list(set(compared))):
                return i
    return -1

week1 = [1,5,6,10]
week2 = [1,3,4,9,10]
n1 = 12

dist1 = [1,2,3,4]
dist2 = [3,5,7]
n2 = 12
print(solution(n2,week2,dist2))



