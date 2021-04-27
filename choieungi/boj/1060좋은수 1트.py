#boj_1060
import heapq

# A,B >0 and integer, A<B
# A<=x<=B x is not in S

# 둘 중 좋은 구간 개수가 적은 것이 더 좋음.  같거나 무한대일 경우에 더 작은 수가 좋은 수
# 홀수번째 리스트 출력 [0::2]

s_size = int(input())

set_num =sorted(set(map(int, input().split())))
n = int(input())

standard = [1] #1<x<S1-1, S1+1<x<S2-1 ... (Sn-1) -1<s<Sn+1
good_num=[]

# 1. 집합 내 원소 출력
for i in set_num:
    print(i,end=' ')
    standard.append(i-1)
    standard.append(i+1)
    n -=1 # 출력한 횟수만큼 빼기

#print(standard)
# 2. 구간 설정 , 힙 자료형 사용?

p=0
while len(standard)>1:
    if n==0:
        break
    i=0
    while i<=len(standard)-2:
        temp = standard[i+1]-standard[i]
        if temp==0:
            heapq.heappush(good_num, (0,standard[i]))
            standard.remove(standard[i])
            standard.remove(standard[i])
            i-=2
        if temp>0:
            heapq.heappush(good_num,(temp+p,standard[i]))
            heapq.heappush(good_num,(temp+p,standard[i+1]))
            standard[i]+=1
            standard[i+1]-=1
        else:
            standard.remove(standard[i])
            standard.remove(standard[i])
        i+=2

    while good_num:
        interval, num = heapq.heappop(good_num)
        print((interval, num), end=' ')

    p+=1
    n-=1

print(good_num)



# for i in range(n):
