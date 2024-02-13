from typing import TypedDict


class Coordinates(TypedDict):
    latitude: float
    longitude: float


def get_coordinates() -> Coordinates:
    return Coordinates(latitude=40, longitude=50)


if __name__ == '__main__':
    c = get_coordinates()
    print(c['latitude'])
