def main():
    print(int(func(40)/func(20)/func(20)))

def func(n):
    if n == 1:
        return 1
    else:
        return n * func(n-1)

if __name__ == "__main__":
    main()
