def main():
    num01_10 = "dummy one two three four five six seven eight nine ten".split()
    num11_19 = "dummy eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
    num20_90 = "dummy dummy twenty thirty forty fifty sixty seventy eighty ninety".split()

    linkedStr = ""
    for i in range(1, 1001):
        num = i
        str = ""
        if num == 1000:
            str += "one thousand"
            num = 0
        if num >= 100:
            str += num01_10[num//100] + " hundred"
            num %= 100
            if num != 0:
                str += " and "
        if num >= 20:
            str += num20_90[num//10]
            num %= 10
            if num != 0:
                str += "-"
        elif num >= 11:
            str += num11_19[num%10]
            num = 0
        if num != 0:
            str += num01_10[num]
        print(str)
        linkedStr += str.replace(" ", "").replace("-", "")
    print(len(linkedStr))

if __name__ == "__main__":
    main()
