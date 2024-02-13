from typing import NamedTuple


class Coordinates(NamedTuple):
    latitude: float
    longitude: float


def get_coordinates() -> Coordinates:
    return Coordinates(20, 30)


if __name__ == '__main__':
    c = get_coordinates()
    print(c)
    # print(c)
    # print(f"Широта: {c.latitude}")
    # print(f"Долгота: {c.longitude}")
    lat, lon = get_coordinates()
    print(f"Широта: {lat}")
    print(f"Долгота: {lon}")
