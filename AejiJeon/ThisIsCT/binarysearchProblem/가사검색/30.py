from bisect import bisect_left, bisect_right

# fro?? -> fro -> 시작점 - 1 반환   frozz 넣어서 ...  -> 마지막 index반환 

def binary_search_opt_left(array,target,start,end):
    onesmaller = start  - 1
    # 못찾음 -> 바로 전 반환
    while True:
        
        if start > end:
            if onesmaller == 0 and target < array[0]:
                return -1
            return onesmaller 
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            onesmaller = mid
            start = mid + 1
        else:
            end = mid - 1


#  5길이 -> 시작점  없으면 None
def get_index_start(array, target_length, start, end):
    while True:

        if start > end:
            return None

        mid = (start + end) // 2
        length = len(array[mid])
        if target_length == length and (mid == 0 or len(array[mid-1]) < target_length):
            return mid
        elif target_length <= length: 
            end = mid - 1
        else:
            start = mid + 1

def get_index_end(array, target_length, start, end):
    n = len(array)
    while True:

        if start > end:
            return None

        mid = (start + end) // 2
        length = len(array[mid])
        if target_length == length and (mid == n-1 or len(array[mid+1]) > target_length):
            return mid
        elif target_length >= length: 
            start = mid + 1
        else:
            end = mid - 1


# [first_i, last_i] 개수  (last_i 포함)
def get_number(first_i, last_i):
    return last_i-first_i+1



def solution(words, queries):
    words.sort()
    words.sort(key=lambda x: len(x))  # 모든 경우 다 길이로 정렬된 배열가지고
    print(words)
    result = [0]*len(queries) # 개수 담기 0개로 세팅
    n = len(words)
    m = len(queries)
    for i in range(m):
        # 길이 시작점 끝점
        print(i)
        query = queries[i]
        print(query)
        start = get_index_start(words, len(query), 0, n-1)
        end = get_index_end(words, len(query), 0, n-1)
        # 단어 길이조차 다름 -> 0
        if start == None or end == None:
            continue
        print(start, end)
        # ????? case
        if query.count('?') == len(query):
            
            result[i] = get_number(start, end)


        # ___?? case
        elif query[-1] == '?':
            first_q = query.index('?')#첫 물음표 위치
            pre = query[:first_q]#앞단어
            print("111111111")
            pre_last = pre + 'z'*(len(query) - first_q) # frozz
            print(pre, pre_last)            

              # 여기 
            print("sssss", pre, start, end)
            first_i = binary_search_opt_left(words,pre,start,end) + 1
            last_i = binary_search_opt_left(words,pre_last,start,end) 
            print(first_i, last_i)
            if first_i > last_i: # 없음
                continue
            result[i] = get_number(first_i, last_i)


        # ???__ case
        elif query[0] == '?':
            print(2222222222)
            last_q = bisect_right(query, '?')
            post = query[last_q:]
            print("post:", post)

            for w in range(start,end+1):
                if post == words[w][last_q:]:
                    
                    result[i] += 1
        
    return result
            
words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words, queries))
            

    
