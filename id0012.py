def main():
    triangleList = [1]
    for i in range(2, 2000000):
        triangleList.append(triangleList[-1] + i)

    maxCount = 0
    for i in triangleList:
        if i % 10 != 0:
            continue
        count = 1
        for j in range(1, int(i/2)+1):
            if i % j == 0:
                count += 1
        if count >= 500:
            print(i)
            break
        if maxCount < count:
            maxCount = count
        print(i, count, maxCount) # watch the progress

if __name__ == "__main__":
    main()
