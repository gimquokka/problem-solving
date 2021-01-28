from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    left_index = bisect_left(a, left_value)
    right_index = bisect_right(a, right_value)
    return right_index - left_index


def solution(words, queries):
    
    leng_arr = [[] for _ in range(10001)]
    reversed_leng_arr = [[] for _ in range(10001)]
    answer = []
    for word in words:
        leng_arr[len(word)].append(word)
        reversed_leng_arr[len(word)].append(word[::-1])

    for i in range(10001):
        leng_arr[i].sort()
        reversed_leng_arr[i].sort()

    for q in queries:
        if q[0] != '?':
            answer.append(count_by_range(leng_arr[len(q)], q.replace('?','a'), q.replace('?','z')))
        else:
            answer.append(count_by_range(reversed_leng_arr[len(q)], q[::-1].replace('?','a'), q[::-1].replace('?','z'))) 

    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words, queries))
