def main():
    for a in range(1, 1000, 1):
        for b in range(1, 1000-a, 1):
            c = 1000 - a - b
            if a ** 2 + b ** 2 == c ** 2:
                print(a * b * c)
                return

if __name__ == "__main__":
    main()
