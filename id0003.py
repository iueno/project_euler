def main():
    num = 600851475143
    primeList = []
    for i in range(3, num, 2):
        if num % i == 0:
            primeList.append(i)
            while num % i == 0:
                num = int(num/i)
        if num == 1:
            break
    print(primeList[-1])

if __name__ == "__main__":
    main()
