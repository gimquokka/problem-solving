from collections import Counter

def solution(s):
    l = len(s)
    min_l = l
    for step in range(1, l//2+1):
        sub_l = 0
        cnt = 1
        prev = s[:step]
        for idx in range(0, l-step, step):
            if(s[idx:idx+step] == s[idx+step:idx+2*step]):
                if (prev == s[idx:idx+step]):
                    cnt += 1
                else:
                    sub_l -= len(str(cnt))
                    cnt = 1
                sub_l += len(s[idx+step:idx+2*step])
            sub_l -= len(str(cnt))
        new_l = l - sub_l        
        min_l = min(new_l, min_l)
    return min_l


# s = "aabbaccc"
# print(solution(s) == 7)
# s = "ababcdcdababcdcd"
# print(solution(s) == 9)
# s = "abcabcdede"
# print(solution(s) == 8)
# s = "abcabcabcabcdededededede"
# print(solution(s) == 14)
# s = "xababcdcdababcdcd"
# print(solution(s) == 17)

s = "bbaabaaaab"
print(solution(s)==8)
# s = "acacacacacacbacacacacacac"
# print(solution(s) == 9)
# s= "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxz"
# print(solution(s) == 5)
