def main():
    map = dict()
    for i in range(1, 10000):
        map[i] = d(i)

    ans = 0
    for k, v in map.items():
        if v in map.keys():
            num = map[v]
            if k == num and k != v:
                print(k, v)
                ans += k
    print(ans)

def d(n):
    divisor = []
    for i in range(1, n):
        if n % i == 0:
            divisor.append(i)
    return sum(divisor)

if __name__ == "__main__":
    main()
