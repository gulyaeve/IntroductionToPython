from typing import Literal


def get_coordinates() -> dict[Literal["longitude", "latitude"], float]:
    return {"latitude": 20, "longitude": 30}


if __name__ == '__main__':
    print(get_coordinates()["latitude"])
    print(get_coordinates()["longitude"])
