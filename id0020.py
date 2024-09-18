def main():
    s = str(func(100))
    ans = 0
    for i in s:
        ans += int(i)
    print(ans)

def func(n):
    if n == 1:
        return 1
    else:
        return n * func(n-1)

if __name__ == "__main__":
    main()
