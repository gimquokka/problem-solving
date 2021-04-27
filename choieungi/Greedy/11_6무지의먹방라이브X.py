def solution(food_times, k):
    temp = 0
    for i in range(k):
        #temp = i%len(food_times)
        food_times[temp]-=1
        while food_times[temp]==0 or food_times[temp]==-1:
            if food_times[temp]==-1:
                food_times[temp] +=1
                temp += 1
            else: #음식이 남지 않았을 때
                if temp ==len(food_times)-1:
                    temp=0
                else:
                    temp+=1
                food_times[temp]-=1
        temp +=1
        temp %= len(food_times)


    answer = temp+1
    return answer

a= [3,1,2]
b=5
print(solution(a,b))

