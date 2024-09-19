def main():
    a, b = 1, 1
    for i in range(3, 10000):
        a, b = b, a + b
        if len(str(b)) == 1000:
            print(i)
            break


if __name__ == "__main__":
    main()
