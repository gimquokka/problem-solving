from collections import Counter

def solution(str1, str2):
    set1 = getMultiSet(str1)
    set2 = getMultiSet(str2)
    
    cnt_set1 = Counter(set1)
    cnt_set2 = Counter(set2)
    
    key_inter = set(cnt_set1.keys()).intersection(set(cnt_set2.keys()))
    key_union = set(cnt_set1.keys()).union(set(cnt_set2.keys()))
    
    inter_num, union_num = 0, 0
    
    for k in key_inter:
        inter_num += min(cnt_set1[k], cnt_set2[k])
    
    for k in key_union:
        a, b = 0, 0
        if k in cnt_set1.keys():
            a = cnt_set1[k]
        if k in cnt_set2.keys():
            b = cnt_set2[k]
        union_num += max(a, b)

    return int(inter_num/union_num*65536) if union_num else 65536

def getMultiSet(s):
    arr = []
    for i in range(len(s)-1):
        if s[i:i+2].isalpha():
            arr.append(s[i:i+2].upper())
    
    return arr


str1 = "FRANCE"
str2 = "french"
print(solution(str1, str2)) 