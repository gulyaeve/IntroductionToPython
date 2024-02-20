import datetime
import pytz
import zoneinfo

# from lesson7.module_my_datetime import my_datetime

if __name__ == '__main__':
    current_datetime = datetime.datetime.now()
    print(current_datetime)
    print(datetime.datetime.time(current_datetime))
    print(datetime.datetime.date(current_datetime))

    current_date = datetime.date.today()
    my_birthday = datetime.date(1988, 10, 30)
    print(current_date - my_birthday)

    days_30 = datetime.timedelta(days=30)
    print(current_date + days_30)

    after_30_days = current_date + days_30

    if after_30_days > current_date:
        print("Такого быть не может")

    print(pytz.all_timezones)
    for tz in pytz.all_timezones:
        if "Moscow" in tz:
            print(tz)

    print(datetime.datetime.utcnow())
    tz_Abidjan = pytz.timezone('Europe/Ulyanovsk')
    print(datetime.datetime.now(tz_Abidjan))
    tz_Moscow = pytz.timezone("Europe/Moscow")
    nowhere_time = datetime.datetime(2024, 2, 19, 9, 47)
    new_now = tz_Moscow.localize(nowhere_time)
    print(new_now.tzinfo)

    print(current_datetime.strftime("%d.%m.%Y %H:%M %A, %w, %B, %p, %j, %W"))

    date_str = "20.02.2024 14:25"
    date_from_str = datetime.datetime.strptime(date_str, "%d.%m.%Y %H:%M")
    print(date_from_str)
    print(date_from_str.strftime("%d.%m.%Y %H:%M"))
    # print(my_datetime.now())

    dt = datetime.datetime.now(zoneinfo.ZoneInfo("Europe/Ulyanovsk"))
    print(dt)
