def num_to_cord(n):
    if n in {1, 2, 3}:
        return (1, n)
    elif n in {4, 5, 6}:
        return (2, n-3)
    elif n in {7, 8, 9}:
        return (3, n-6)
    elif n == 0:
        return (4, 2)


'''
# 이와 같은 방식으로 하면 더 간결할 듯!
key_dict = {1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0),0:(3,1),'#':(3,2)}

'''


def solution(numbers, hand):
    ans = ''
    l_pos = (4, 1)
    r_pos = (4, 3)
    for num in numbers:
        if num in {1, 4, 7}:
            ans += 'L'
            l_pos = num_to_cord(num)
        elif num in {3, 6, 9}:
            ans += 'R'
            r_pos = num_to_cord(num)
        else:
            num_pos = num_to_cord(num)
            l_dist = abs(num_pos[0]-l_pos[0]) + abs(num_pos[1]-l_pos[1])
            r_dist = abs(num_pos[0]-r_pos[0]) + abs(num_pos[1]-r_pos[1])
            # 1. 같은 경우
            if l_dist == r_dist:
                if hand == 'right':
                    ans += 'R'
                    r_pos = num_pos
                else:
                    ans += 'L'
                    l_pos = num_pos
            # 2. 왼손이 더 가까운 경우
            elif l_dist < r_dist:
                ans += 'L'
                l_pos = num_pos
            # 3. 오른손이 더 가까운 경우
            else:
                ans += 'R'
                r_pos = num_pos
    # 정답 반환
    return ans
