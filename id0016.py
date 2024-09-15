def main():
    s = str(2 ** 1000)
    ans = 0
    for i in s:
        ans += int(i)
    print(ans)

if __name__ == "__main__":
    main()
