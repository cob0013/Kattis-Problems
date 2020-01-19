from datetime import date
def main():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    d, m = map(int, input().split())
    day = date(2009, m, d)
    print(days[day.weekday()])


if __name__ == "__main__":
     main()

