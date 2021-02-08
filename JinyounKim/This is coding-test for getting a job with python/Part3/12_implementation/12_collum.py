def xy_to_ij(x, y):
    i = n - y
    j = x
    
    return i, j

def install_col(data, x, y):
    i, j = xy_to_ij(x, y)
    if data(i, j) == 1:
        data() = 1
    


def install_boo(data, x, y):
    pass

def uninstall_col(data, x, y):
    pass

def uninstall_boo(data, x, y):
    pass


def solution(n, build_frame):
    answer = [[]]
    data = [0]*(n+1)

    # Bottom initiallize
    for i in range(n+1):
        data[n+1][i] = 1


    answer.sort()
    return answer