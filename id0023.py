def main():
    excess = []
    for i in range(1, 28123):
        if check_excess(i):
            excess.append(i)

    numbers = [n for n in range(1, 28123)]
    for i in range(0, len(excess)):
        for j in range(i, len(excess)):
            if excess[i] + excess[j] in numbers:
                numbers.remove(excess[i] + excess[j])
            elif excess[i] + excess[j] > 28123:
                break
    print(sum(numbers))

def check_excess(n):
    divisor = []
    for i in range(1, n):
        if n % i == 0:
            divisor.append(i)
    return n < sum(divisor)

if __name__ == "__main__":
    main()
