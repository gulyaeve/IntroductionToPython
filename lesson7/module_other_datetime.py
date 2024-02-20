import arrow
import maya
from dateutil import parser


if __name__ == '__main__':
    current_datetime = arrow.now()
    print(current_datetime)
    # print(current_datetime.to('UTC'))

    dt = maya.parse("2024-02-19T19:15:59.335160+03:00")
    print(dt)
    dt = maya.parse("2024-02-19T19:15:59.335160+03:00").datetime()
    print(dt)
    print(dt.date())
    print(dt.time())

    dt_new = parser.parse("Mon, 19 Feb 2024 16:15:59 GMT")
    dt_new_2 = parser.parse("2024-02-19T19:20:46.313648+03:00")
    dt_new_3 = parser.parse("20.02.2024 14:25")
    dt_new_4 = parser.parse("2024-02-19 19:21:39.851798")

    print(dt_new)
    print(dt_new_2)
    print(dt_new_3)
    print(dt_new_4)
