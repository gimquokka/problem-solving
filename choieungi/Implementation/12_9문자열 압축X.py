n = input()
string = []
num = []

def solution(s):
    s_sep = [0]*len(s)
    for i in range(len(s)):
         s_sep[i] = s[i]

    for i in range(len(s)):
        for j in range(i):
            if



    answer = 0
    return answer

#실패한 원인: 연속된 문자열을 비교하는 코드를 짜지 못 햇음. 예를 들면 한개 단위로 잘랐을 때 num[0] = num[1] num[1]=num[2] 이런 식으로 짜고 두개 단위로 잘랐을 때 num[1],num[2]=num[3],num[4]
#이런 식으로 만드는 코드를 짜기 어려웠기 때문