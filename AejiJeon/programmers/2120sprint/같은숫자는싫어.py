# my code
def solution(arr):
    answer = []
    i, j = 0, 1 
    while len(arr) > j:
        
        if  arr[i] == arr[j]:
            j += 1
        else:
            answer.append(arr[i])
            i = j
            j += 1
    answer.append(arr[i])
    return answer


# 2
# def no_continuous(s):
#     # 함수를 완성하세요
#     return [s[i] for i in range(len(s)) if s[i] != s[i+1:i+2]]