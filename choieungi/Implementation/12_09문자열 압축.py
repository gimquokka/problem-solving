
# n개 단위로 잘라 압축을 진행할 때 가장 짧게 압축된 문자열의 길이를 찾는 문제
# 1개 단위 aabbccd --> 2a2b2cd 2개 ababccd --> 2abccd
# 압축이 안되서 최솟값이 없으면, 그 문자열의 길이가 답

def solution(s):
    temp_num = 1                                        #중복 개수를 세기 위한 변수
    answer = len(s)
    for i in range(1,(len(s)//2)+1):                    #얼마나 자를 것인가
        temp = ''                                       # 일시적으로 문자열을 넣기 위한 변수, i단위로 문자열의 길이를 구했으니 초기화 해 i+1 단위 문자열을 구하기 시작
        for j in range(0,len(s),i):                     #(j=0 ; j<len(s) ; j= j+ i)
            if s[j:j + i] == s[j + i:j + 2 * i]:
                temp_num+=1
            else:
                if temp_num>1:                          #문자열이 중복될 때
                    temp += (str(temp_num)+s[j:j + i])
                elif temp_num ==1:                      #문자열이 중복되지 않을 때
                    temp += (s[j:j + i])
                temp_num=1                              #출력을 했으니 중복 세는 변수를 초기화
        answer = min(len(temp), answer)
    return answer

q='aaaeeasdffffasdf'
print(solution(q))
