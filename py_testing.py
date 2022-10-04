# coded by h4sski

from datetime import date
import calendar


def main():
    FIRST = 1
    SECOND = 1
    THIRD = 1
    FOURTH = 1
    for i in range(4):
        FIRST += 1 * i
        print(f'First =\t\t{FIRST}')
        SECOND += 2 * i
        print(f' Second =\t {SECOND}')
        THIRD += 3 * i
        print(f'  Third =\t  {THIRD}')


if __name__ == '__main__':
    # main()
    today = date.today()
    # print(today.month)
    c = calendar.TextCalendar(calendar.MONDAY)
    str = c.formatmonth(today.year, today.month)
    # print(str)
    # str = c.formatmonth(today.year(), today.month())
    # print(calendar)

    # for t in range(1, 13):
    #     print(f't = {t}')
    #     if t in [1, 3, 5, 7, 8, 10, 12]:
    #         print(31)
    #     elif t == 2:
    #         print(28)
    #     else:
    #         print(30)

dictionary = {}
list = [0, 1, 2, 3, 4, 5, 66]
for i, v in enumerate(list):
    dictionary[i].append(v)

print(dictionary)
