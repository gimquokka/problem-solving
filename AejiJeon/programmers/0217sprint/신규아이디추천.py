def solution(id):
    
    # 1
    id = id.lower()
    
    # 2
    l = len(id)
    i = 0
    while i <= l-1:
        if id[i] in ['-', '_', '.'] or '0' <= id[i] <= '9' or 'a' <= id[i] <= 'z':
            i += 1
        else:
            id = id[:i] + id[i+1:]
            l -= 1    
    
    # 3
    c = 0
    i = 0
    while i <= l-1:
        if id[i] == '.':
            c += 1
            i += 1
            continue
        elif c >= 2:
            id = id[:i-c] + '.' + id[i:]
            l -= c - 1
            i -= c - 2
            c = 0
        else:
            c = 0
            i += 1
    if c >= 2:
        id = id[:i-c] + '.' + id[i:]
    
    # 4
    if id[0] == '.':
        id = id[1:]
    if len(id) > 0 and id[-1] == '.':
        id = id[:-1]
    
    # 5
    if len(id) == 0:
        id += 'a'
    
    # 6
    if len(id) >= 16:
        id = id[:15]
        if id[-1] == '.':
            id = id[:-1]
    
    # 7       
    while len(id) <= 2:
        id += id[-1]
            
    return id