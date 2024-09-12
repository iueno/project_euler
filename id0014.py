def main():
    maxCount = 0
    ans = 0
    for i in range(1, 1000000):
        count = 1
        n = i
        while n != 1:
            if n % 2 == 0:
                n = n / 2
            else:
                n = 3 * n + 1
            count += 1
        if maxCount < count:
            maxCount = count
            ans = i
    print(ans)

if __name__ == "__main__":
    main()
