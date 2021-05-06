def main():
    x = input()
    print('YES' if x.count('(') == x.count(')') else 'NO')


if __name__ == "__main__":
    main()
