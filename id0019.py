import datetime

def main():
    dt = datetime.datetime(1901, 1, 1)
    ans = 0
    while dt.year <= 2000:
        if dt.weekday() == 6 and dt.day == 1:
            ans += 1
        dt = dt + datetime.timedelta(days=1)
    print(ans)

if __name__ == "__main__":
    main()
