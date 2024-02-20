import calendar


if __name__ == '__main__':
    print(calendar.Calendar(0))

    for day in calendar.Calendar(0).itermonthdays(2023, 2):
        print(day)

    cal = calendar.TextCalendar(3)
    cal.prmonth(2024, 2)

    cal_2 = calendar.HTMLCalendar()
    feb = cal_2.formatmonth(2024, 2)
    print(feb)

    with open("feb.html", "w") as file:
        file.write(feb)

    cal_3 = calendar.HTMLCalendar()
    year = cal_3.formatyearpage(2024)
    with open("2024.html", "wb") as file:
        file.write(year)
