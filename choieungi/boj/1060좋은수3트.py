#boj_1060
import heapq
import math
import copy
# A,B >0 and integer, A<B
# A<=x<=B x is not in S

# 둘 중 좋은 구간 개수가 적은 것이 더 좋음.  같거나 무한대일 경우에 더 작은 수가 좋은 수
# 홀수번째 리스트 출력 [0::2]
def cnt_interval(start, end, num, cnt=0):
    while start <= num:
        if start < num:
            cnt += end - (num - 1)

        elif start == num:
            cnt += end - num
        start += 1
    return cnt


s_size = int(input())

set_num =sorted(set(map(int, input().split())))
n = int(input())
to_print =n
standard = [1] #1<x<S1-1, S1+1<x<S2-1 ... (Sn-1) -1<s<Sn+1
good_num=[]
real_good_num =[]

# 1. 집합 내 원소 출력
temp =[ ]
for i in set_num:
    temp.append(i)
    standard.append(i-1)
    standard.append(i+1)
    n -=1 # 출력한 횟수만큼 빼기

for i in range(len(set_num)-1):
    if temp[i+1]-temp[i]==2:
        temp.append(temp[i]+1)
        standard.remove(temp[i]+1)
        standard.remove(temp[i]+1)

temp.sort()
for i in temp:
    real_good_num.append(i)

#print(standard)
# 2. 구간 설정 , 힙 자료형 사용?
#연산 횟수
#print((100-s_size)/(s_size*2))

cal = math.ceil((100-s_size)/(s_size))
#print(cal)

boundary = copy.deepcopy(standard)
i=0
while True :
    if cal ==0:
        break
    i=0
    while i<= len(standard)-2:
        interval = cnt_interval(boundary[i], boundary[i + 1], standard[i])
        if standard[i+1]-standard[i] > 0:
            heapq.heappush(good_num, (interval, standard[i]))
            heapq.heappush(good_num, (interval, standard[i+1]))
        elif standard[i + 1] - standard[i] == 0:
            heapq.heappush(good_num, (interval, standard[i]))
        standard[i] += 1
        standard[i + 1] -= 1
        i+=2
    cal-=1


#print(good_num)

while good_num:
    if n<=0:
        break
    interval, num = heapq.heappop(good_num)
    real_good_num.append(num)
    n-=1


infinite = standard.pop()
while n>0:
    real_good_num.append(infinite)
    infinite+=1
    n-=1

for i in range(to_print):
    print(real_good_num[i],end=' ')


#print(good_num)



# for i in range(n):
