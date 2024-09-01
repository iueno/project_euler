def main():
    count = 2 # initial count of prime number "2, 3"
    primeList = [2, 3]
    for num in range(5, 100000000000, 2):
        for i in primeList:
            if num % i == 0:
                break
            elif i == primeList[-1]:
                primeList.append(num)
                count += 1
                if count == 10001:
                    print(num)
                    return

if __name__ == "__main__":
    main()
