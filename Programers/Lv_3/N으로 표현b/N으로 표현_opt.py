def solution(N, number):
    # When number = N
    if N == number:
        return 1
    
    # 0. Init ans
    ans = -1

    # 1. Initialize Set
    s = [set() for _ in range(8)]

    # 2. Add basic N*i numbers
    for i in range(1, 9):
        s[i-1].add(int(str(N)*i))

    # 3. DP
    for i in range(1, 8):
        ''' 
        range(i)의 경우 3 => (0, 2), (1, 1), (2, 0) 중심을 기준으로 중복 발생
        range(i//2 + 1)의 경우 3 => (0, 2), (1, 1 ) 
        '''
        for j in range(i//2 + 1):
            for op1 in s[j]:
                for op2 in s[i-j-1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op2 - op1)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1//op2)
                    if op1 != 0:
                        s[i].add(op2//op1)
            if number in s[i]:
                ans = i + 1
                return ans
    
    return ans