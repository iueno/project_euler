import csv

def main():
    names = []
    with open("p022_names.txt") as f:
        reader = csv.reader(f)
        for row in reader:
            for name in row:
                names.append(name)
    names.sort()

    ans = 0
    for i, name in enumerate(names):
        score = 0
        for s in name:
            score += ord(s) - 64
        score = score * (i + 1)
        ans += score
    print(ans)


if __name__ == "__main__":
    main()
