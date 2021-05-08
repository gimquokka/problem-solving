def search_range(query, length):
    index = list(filter(lambda x: query[x] == '?', range(length)))
    if index:
        left = index[0]
        right = index[-1]
        if left == 0:
            return right+1, length-1
        else:
            return 0, left-1
    else: return 0, length-1

def get_start(len_arr, s, e, target, start_index, end_index):
    m = (s+e)//2
    result = 0
    while s <= e:
        if str(len_arr[m][start_index:end_index+1]) == target:
            e = m-1
            result = m
        elif str(len_arr[m][start_index:end_index+1]) > target:
            e = m-1
        else:
            s = m+1
    return result
def get_end(len_arr, s, e, target, start_index, end_index):
    m = (s+e)//2
    result = 0
    while s <= e:
        if str(len_arr[m][start_index:end_index+1]) == target:
            s = m+1
            result = m
        elif str(len_arr[m][start_index:end_index+1]) > target:
            e = m-1
        else:
            s = m+1
    return result

def solution(words, queries):
    answer = []
    len_arr = dict()
    
    for word in words:
        i = len(word)
        len_arr[i].append(len_arr)

    for query in queries:
        length = len(query)
        start_index, end_index = search_range(query, length)

        len_arr[length].sort()
        same_len_num = len(len_arr[length])
        s = 0
        e = same_len_num-1
        start = get_start(len_arr[length], s, e, query[start_index:end_index], start_index, end_index)
        end = get_start(len_arr[length], s, e, query[start_index:end_index], start_index, end_index)
        answer.append(end-start)
        
    return answer