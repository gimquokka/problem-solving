# 10101100 10100000 00100000 00000000  3hl

s_lst = list(map(int, input()))

count = [0, 0]  # count[0] : count 0's, count[1] : count 1's

for i in range(len(s_lst)):        

    if i != 0:
        if s_lst[i-1] == s_lst[i]:
            continue 

    count[s_lst[i]] += 1

print(min(count)) 
    
