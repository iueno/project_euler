def main():
    max_idx, max_len = 0, 0
    for i in range(2, 1000):
        a = 1
        l = []
        while True:
            remainder = a % i
            if remainder == 0:
                break
            elif remainder in l:
                if max_len < len(l):
                    max_len = len(l)
                    max_idx = i
                break
            else:
                l.append(remainder)
                a = remainder * 10
    print(max_idx)


if __name__ == "__main__":
    main()
