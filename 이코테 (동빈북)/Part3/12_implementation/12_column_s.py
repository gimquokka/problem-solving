def possible(build_frame):
    for frame in build_frame:
        x, y, stuff = frame
        if stuff == 0:
            if (y == 0) or ([x, y-1, 0] in build_frame) or ([x, y, 1] in build_frame) or ([x-1, y, 1] in build_frame):
                continue
            else:
                return False
        else:
            if ([x, y-1, 0] in build_frame) or ([x+1, y-1, 0] in build_frame) or ([x-1, y, 1] in build_frame and [x+1, y, 1] in build_frame) :
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    answer = []

    for frame in build_frame:
        x, y, stuff, operator = frame
        now = [x, y, stuff]
        if operator == 0:
            answer.remove(now)
            if not possible(answer):
                answer.append(now)
        else:
            answer.append(now)
            if not possible(answer):
                answer.remove(now)
    
    answer.sort()
    return answer

n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

print(solution(n, build_frame))