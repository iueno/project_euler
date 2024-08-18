def main():
    for num in range(2520, 100000000000, 20):
        for i in range(20, 6, -1):
            if num % i != 0:
                break
            else:
                if i == 7:
                    print(num)
                    return

if __name__ == "__main__":
    main()
