def possible(result):
    for x, y, stuff in result:
        if stuff == 0:
            if y == 0 or [x-1, y, 1] in result or [x,y,1] in result or [x,y-1,0] in result:
                continue
            return False
        if stuff == 1:
            if [x,y-1,0] in result or [x+1, y-1,0] in result or ([x-1,y,1] in result and [x+1,y,1] in result):
                continue
            return False
    return True



def solution(n, buildframe):
    result = []
    for frame in build_frame:
        x, y, a, op = frame
        if op == 0:
            result.remove([x,y,a])
            if not possible(result):
                result.append([x,y,a])
        
        if op == 1:
            result.append([x,y,a])
            if not possible(result):
                result.remove([x,y,a])
    
    return sorted(result)      # lexicographic sorting으로 안해도 되나..?

build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
print(solution(len(build_frame),build_frame))