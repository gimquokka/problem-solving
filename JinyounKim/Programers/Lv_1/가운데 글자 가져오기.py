def solution(s):

    length = len(s)
    mid = length//2-1
    if length % 2 == 0:
        return s[mid:mid+2]
    else:
        return s[mid+1]

    # 이렇게 풀면 if/else가 필요없음...
    # return str[(len(str)-1)//2:len(str)//2+1]
