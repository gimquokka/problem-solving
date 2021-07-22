from bisect import bisect_left, bisect_right

def count_by_range(arr, left, right):
    s = bisect_left(arr, left)
    e = bisect_right(arr, right)    
    return e - s

def solution(words, queries):
    a = [[] for _ in range(10001)]
    ra = [[] for _ in range(10001)]

    for word in words:
        length = len(word)
        a[length].append(word)
        ra[length].append(word[::-1])
        
    for i in range(10001):
        a[i].sort()
        ra[i].sort()
    
    result = []
    for query in queries:
        length = len(query)
        if query[0] == "?":
            result.append(count_by_range(ra[length], query[::-1].replace("?", "a"), query[::-1].replace("?", "z")))
        else:
            result.append(count_by_range(a[length], query.replace("?", "a"), query.replace("?", "z")))
            
    return result