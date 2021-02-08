'''
문제 설명

solution 함수에
- food_times = [3, 1, 4] 1 => [2, 0, 3]
- k = 5 와 같은 Input이 들어 오면

각각 인덱스에서 0까지 1씩 감소하다 총 5만 큼 감소가 되고,
이후 k+1 될 좌표를 반환하면 됨.
'''

# Use heapq lib for min heap structure 
import heapq

def solution(food_times, k):
    # Return -1 if total sum of food_times is smaller than k
	# sum => O(n)
	if sum(food_times) <= k: 
            return -1
	
    q = []
    l = len(food_times)
    
	# Add (element, index) tuple in q
    
	# O(n * log(n)) n times x push heap
	for i in range(l):
        heapq.heappush(q, (food_times[i], i+1))
    
    prev = 0
    # heapq.heapify(q)하지 않아도 q[0][0]만큼은 항상 min val !
	# 따라서 heapify 할 필요가 없음. q를 while 전에 heappop할 필요가 없음
	# Time complexity = O(k-n)
	q[0][0]*l < k
	while l*(q[0][0] - prev) < k: # <=, < whatever
        now = heapq.heappop(q)[0]
		val = now - prev # Consider previously removed element
        k -= val*l # sub k from val*l that is for remove que element
        prev = now # Renewal prev
        l -= 1 # Bcz one of que element is removed from stack
    
	# For index order sorted
	# O(nlogn)
    q.sort(key = lambda x : x[1])
    
	 # ----> --> like this way search k+1 th index
	answer = q[k%l][1]
    return answer

# P.S 
# 1. Binary Search way in efficient and unintuitive
# https://velog.io/@meantint/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%AC%B4%EC%A7%80%EC%9D%98-%EB%A8%B9%EB%B0%A9-%EB%9D%BC%EC%9D%B4%EB%B8%8C

# 2. Brute force? k*l
