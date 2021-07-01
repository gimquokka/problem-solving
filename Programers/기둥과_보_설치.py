def possible(build_frame):
    done = []
    
    for x, y, _type in build_frame:
        if _type == 0:
            if y == 0 or ([x+1, y, 1] in done) or ([x, y, 1] in done) or ([x,y-1, 0] in done):
                continue
            else:
                return False
        else:
            if [x, y, 1] or ()
        
    

def solution(build_frame):
    pass