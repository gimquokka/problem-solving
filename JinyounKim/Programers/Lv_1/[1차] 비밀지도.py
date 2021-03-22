def solution(n, arr1, arr2):
    ans = []
    for a, b in zip(arr2, arr1):
        str_bin = str(bin(a|b))[2:]
        str_bin = str_bin.rjust(n, "0")
        '''
        # 이 코드를 rjust로 대체 가능
        len_bin = len(str_bin)
        if len_bin < n:
            str_bin = ' '*(n-len_bin) + str_bin
        '''    
        ans.append(str_bin.replace("1", "#").replace('0', ' '))
    # print(ans)
    return ans

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n, arr1, arr2))