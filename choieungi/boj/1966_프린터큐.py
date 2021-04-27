#boj_1966
import copy

cases = int(input())


for _ in range(cases):
    n,m = map(int,input().split())
    document = list(map(int,input().split()))
    index = [i for i in range(n)]
    index[m] = 'target'
    real_queue = [ ]
    cnt = 0
    for i in enumerate(document):
        real_queue.append(i)

    while True:
        if document[0] == max(document):
            cnt += 1

            if index[0] =='target':
                print(cnt)
                break
            else:
                del document[0]
                del index[0]
        elif document[0] < max(document):
            document.append(document.pop(0))
            index.append(index.pop(0))


# pop vs del , pop은 index를 반환하고 del은 인덱스를 반환하지 않는다. 그래서 del이 더 바름
# queue는 mutable인가...?


