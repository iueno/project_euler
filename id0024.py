import itertools

def main():
    num = ['0','1','2','3','4','5','6','7','8','9']
    p_list = list(itertools.permutations(num))
    print("".join(p_list[999999]))

if __name__ == "__main__":
    main()
