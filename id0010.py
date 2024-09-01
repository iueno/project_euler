def main():
    primeList = [2, 3]
    for num in range(5, 2000000, 2):
        print(num)
        for i in primeList:
            if num % i == 0:
                break
            elif i == primeList[-1]:
                primeList.append(num)
    print(sum(primeList))

if __name__ == "__main__":
    main()
