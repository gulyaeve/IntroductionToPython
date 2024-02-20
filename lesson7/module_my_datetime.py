from datetime import datetime


class my_datetime(datetime):
    def __str__(self):
        date = self.isoformat(sep=' ')
        date = self.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
        return date.strftime("%d.%m.%Y %H:%M")
