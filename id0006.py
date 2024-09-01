def main():
    a, b = 0, 0
    for num in range(1, 100+1, 1):
        a += num ** 2
        b += num
    print(b ** 2 - a)

if __name__ == "__main__":
    main()
