import heapq

food_times =[8, 6, 4]   
k = 15
l = len(food_times)
q=[]
for i in range(l):
    heapq.heappush(q, (food_times[i], i))           
dec_time = 0
while q:
    time, index = heapq.heappop(q)      
    time -= dec_time
    new_k = k - time*l
    print(new_k)
    if new_k < 0:
        q.append((time+dec_time, index))
        break
    dec_time += time
    k = new_k
    l -= 1

if q:
    result = sorted(q, key=lambda x:x[1])
    print(result)
    print(k)
    print(result[k%l][1]+1)
else:
    print(-1)   

