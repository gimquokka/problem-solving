import re

def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if not re.findall("[^a-zA-Z]+", str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if not re.findall("[^a-zA-Z]+", str2[i:i+2])]
    
    inter_key = set(str1)&set(str2)
    union_key = set(str1)|set(str2)
    
    if not union_key:
        return 65536
    
    inter_num = sum([min(str1.count(k), str2.count(k)) for k in inter_key])
    union_num = sum([max(str1.count(k), str2.count(k)) for k in union_key])
    
    return int((inter_num/union_num)*65536)
    

str1, str2 = "aa1+aa2", "AAAA12"

print(solution(str1, str2))

