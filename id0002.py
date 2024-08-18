def main():
    a, b = 1, 2
    ans = 2
    while b <= 4000000:
        nextNum = a + b
        if nextNum % 2 == 0:
            ans += nextNum
        a, b = b, nextNum
    print(ans)

if __name__ == "__main__":
    main()