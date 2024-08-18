def main():
    productList = []
    for a in range(999, 100, -1):
        for b in range(999, 100, -1):
            product = a * b
            if str(product) == str(product)[::-1]:
                productList.append(product)
                break
    print(max(productList))

if __name__ == "__main__":
    main()
