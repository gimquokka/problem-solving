from bisect import bisect_left, bisect_right

# Implement count function using bisect lib
def count_by_range(a, left, right):
    """
    # Motive #
    "as" > "vd" => False
    python support str comparision

    # Input #
    a: array, 
    left: searched element left-side, 
    right: "" right-side

    # Output #
    number of element between left and right

    # Time complexity #
    O(log(n))
    """
    left = bisect_left(a,left)
    right = bisect_right(a, right)
    return right-left
    

def solution(words, queries):
    """
    # Input #
    words: array with all word, 
    queries: object for searching

    # Output #
    answer: array with numbers that is occurance count in words array

    # Time complexity #
    W: length of words
    w: small w that is stisfied [eq: w1 + w2 + w3 ..... = W]
    Q: "" of queries
    C: constant (= Max length of word)
    
    O(2C+2W+2Clog(w)+Qlog(w))
    => O(C+W+Clog(w)+Qlog(w))
    """
    answer = []
    # Time complexity = O(2C) #
    a = [[] for _ in range(10001)]
    # For the cases of ??abc. Bcz It is imposible binary searching (= BS)
    reverse_a = [[] for _ in range(10001)]

    # Asign input element to a, reverse_a length by length
    for word in words:
        length = len(word)
        a[length].append(word)
        reverse_a[length].append(word[::-1])
    
    # Sort all element in a, reverse_a for BS
    for i in range(10001):
        a[i].sort()
        reverse_a[i].sort()
    
    # Process queries using count_by_range func
    for q in queries:
        result = 0
        length = len(q)
        # In case of "?" located in prefix
        if q[0] == '?':
            result = count_by_range(reverse_a[length], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        # "" "?" in suffix 
        else:
            result = count_by_range(a[length], q.replace('?', 'a'), q.replace('?', 'z'))
        
        # append num of element matched with quiries at answer array
        answer.append(result)

    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))