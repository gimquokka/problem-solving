def solution(bridge_length, weight, truck_weights):
    time = 0
    ## 차가 1개일 때
    if len(truck_weights) == 1 :
        return bridge_length + 1
    ## 차가 1개 초과일 때
    else :
        ## on: 다리 위의 차 상태, bridge_length만큼 0으로 초기화
        sum = 0
        on = []
        for i in range(bridge_length-1) :
            on.append(0)

        ## 첫 번째 차
        on.append(truck_weights.pop(0))
        sum+=on[bridge_length-1]
        time += 1
        
        ## 두 번째 차부터, truck_weights 전부 넣기.
        while truck_weights :
            
            if (sum+truck_weights[0]) <= weight :
                on.append(truck_weights.pop(0))
                sum=sum-on[0]+on[bridge_length]
                del(on[0])
                time += 1
            ## 차가 하나 빠지고 하나 들어오는 경우 len(on) 줄어드는 문제 해결
            else : 
                sum=sum-on[0]
                del(on[0])
                if (sum+truck_weights[0]) <= weight :
                    on.append(truck_weights.pop(0))
                    sum=sum+on[bridge_length-1]
                else :
                    on.append(0)
                time += 1

        return time+bridge_length


solution(2,10,[7,4,5,6])
