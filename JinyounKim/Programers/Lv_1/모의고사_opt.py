def solution1(answers):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx % len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx % len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx % len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result


def solution(answers):
    answer = []
    
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0]*3
    for idx, ans in enumerate(answers):
        if ans == pattern1[idx%5]:
            score[0] += 1
        if ans == pattern2[idx%8]:
            score[1] += 1
        if ans == pattern3[idx%10]:
            score[2] += 1
        
    max_score = max(score)
    for idx, s in enumerate(score):
        if s == max_score:
            answer.append(idx+1)
    
    return answer
        

