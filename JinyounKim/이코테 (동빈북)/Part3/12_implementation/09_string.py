"""
너무 정신 없게 풀었는데,
이렇게 좀 까다로운 문제를 어떻게 제한 시간내에 풀 수 있을지 연습하자!
"""
def solution(s):
	n = len(s)
	answer = n
	for step in range(1, (n//2)+1):
		compressed = ''
		count = 1
		for i in range(0, n-1+step, step):
			# print(i)
			if s[i:i+step] == s[i+step:i+2*step]: # 8 - 1
				count += 1
				# print(count)
			else:
				if count >= 2:
					compressed += str(count)+s[i:i+step]
					count = 1
				else:
					compressed += s[i:i+step]
		# print("step:", step, "compressed:",compressed)
		answer = min(answer, len(compressed))
			
	return answer

# s = "aabbaccc" # 7
# print(solution(s))

s = "ababcdcdababcdcd" # 9
print(solution(s))