def main():
    data = input()
    print('YES' if data.count('(') == data.count(')') else 'NO')


if __name__ == "__main__":
    main()
