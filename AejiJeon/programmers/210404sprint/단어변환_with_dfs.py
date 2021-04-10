# dfs로 구현 
import copy

# parameter가 너무 만다..
def dfs(now, target, count, words, possible_words, words_dic, visited):
    global result
    visited = copy.deepcopy(visited)
    now_idx = words_dic[now]
    visited[now_idx] = True

    # begin -> target 바꾸기 성공
    if now == target:
        result = min(result, count)
        return

    for possible_word in possible_words[now_idx]:
        # possible_word에 해당하는 index 구해줌
        next_idx = words_dic[possible_word]
        if not visited[next_idx]:
            dfs(
                words[next_idx],
                target,
                count + 1,
                words,
                possible_words,
                words_dic,
                visited,
            )


# word1, word2의 알파벳 구성이 1개만 다른지 체크
def is_one_diff(word1, word2):
    count = 0
    for a, b in zip(word1, word2):
        if a != b:
            count += 1
    return True if count == 1 else False


def solution(begin, target, words):
    global result
    # 각 word마다 index 찾아주는 dictionary 선언
    words_dic = {words[i]: i for i in range(len(words))}
    possible_words = [[] for _ in range(len(words))]

    # i 번째 word와 알파벳 구성이 1개가 다른 words 찾아줌
    for i in range(len(words)):
        for word in words:
            if is_one_diff(words[i], word):
                possible_words[i].append(word)

    visited = [False] * len(words)
    for word in words:

        # begin -> 한 개의 알파벳만 바뀐 단어들로 바꿔줌
        if is_one_diff(begin, word):
            dfs(word, target, 1, words, possible_words, words_dic, visited)

    return result if result != int(1e9) else 0


# global 변수 선언 -> begin이 target으로 바뀔 때마다 최솟값으로 업데이트
# gobal 변수 사용하지 않고 풀어보기
result = int(1e9)
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
result = int(1e9)
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))