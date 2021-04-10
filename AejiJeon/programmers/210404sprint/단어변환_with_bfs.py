# bfs로 구현 without global variable
from collections import deque

# current word와 알파벳 구성이 1개만 다른 words를 담은 array를 return
def get_possible_words(current, words):
    arr = []
    for word in words:

        count = 0
        for a, b in zip(current, word):
            if a != b:
                count += 1

        if count == 1:
            arr.append(word)
    return arr


# bfs 구현
def solution(begin, target, words):
    # begin word부터 해당 단어를 만들기 위해
    # 단어를 바꿔야 하는 최소 횟수를 value값으로 가지는 dictionary 선언
    dist_dic = {begin: 0}
    q = deque([begin])

    while q:
        current = q.popleft()
        for possible_word in get_possible_words(current, words):
            if possible_word not in dist_dic:
                # begin -> possible_word로 바꾸기 위한 최소 변환 횟수를 구해줌
                dist_dic[possible_word] = dist_dic[current] + 1
                q.append(possible_word)

    return dist_dic[target] if target in dist_dic else 0


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))