def main():
    n = int(input())
    score = dict()

    for i in range(n*n):
        data = list(map(int, input().split()))
        for j in data[2:]:
            if j in score:
                score[j] = max(score[j], data[0])
            else:
                score[j] = data[0]

    print(sum(score[key] for key in score))


if __name__ == "__main__":
    main()
