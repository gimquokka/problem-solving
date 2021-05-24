import re
def solution(str1, str2):
    small_dict = dict()
    
    if len(str1) >= len(str2) :
        long = str1
        short = str2
    else :
        long = str2
        short = str1
        
    for i in range(len(short)-2):
        str_key = short[i:i+2]
        str_key = re.sub('[^A-Za-z]', '', str_key)
        str_key = str_key.upper()
        if len(str_key) != 2:
            continue
        elif str_key in small_dict:
            small_dict[str_key] +=1 
        else:
            small_dict[str_key] = 1
            
    set_union = 0
    set_intersection = 0
    for j in range(len(long)-2):
        str_key = long[j:j+2]
        str_key = re.sub('[^A-Za-z]', '', str_key)
        str_key = str_key.upper()
        if len(str_key) != 2:
            continue
        elif str_key in small_dict:
            if small_dict[str_key] == 0:
                set_union = set_union+1
            else:
                set_intersection+=1
                small_dict[str_key]-=1
        else :
            set_union+=1
    set_union +=  set_intersection + sum(small_dict.values())
    return int((set_intersection / set_union) * 65536) if not set_union else 65536