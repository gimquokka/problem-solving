def solution(s):
    half_length = len(s)//2 #aabbaccc l = 8   half_l = 4
    result = len(s)
    for div_leng in range(1, half_length+1):  # 1
        _s = s[:]
        left = len(s)%div_leng
        if left != 0:
            _s=s[:len(s)-left]
        p_result = 0
        length = 1 
        start_i = div_leng  # 1
        start = _s[0:div_leng]
        print('div_leng:', div_leng)
         # start = a
        while True: # 3 <= 7
            # start_i = div_leng  # 1
            # start = s[start_i:start_i+div_length]
            print('start string:',start)
            comp_str = _s[start_i:start_i+div_leng]
            
            print('compare string:', comp_str)
            # start_i = start_i+div_leng
            if start == comp_str:    # a == s[2:3] = b
                length += 1    # 반복 횟수    2
                start_i = start_i+div_leng    # 1+1=2
                if start_i > len(_s)-div_leng:
                    p_result += div_leng + len(str(length))
                    break


            else:

                if length == 1:   # 2
                    p_result += div_leng 
                else: 
                    p_result += div_leng + len(str(length)) # 1 고치기! 19 ->2  5->1 자릿수로   2a
                
                length = 1
                start = comp_str
                start_i = start_i+div_leng
                if start_i > len(_s) - div_leng:
                    p_result += div_leng 
                    break
                print('p_result:', p_result)

        p_result += left 
        print('lsat_p_result:', p_result)
        result = min(result, p_result)


    return result

print(solution('xababcdcdababcdcd'))

