from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Coordinates:
    latitude: float
    longitude: float

    def __str__(self):
        return (f"Latitude: {self.latitude}\n"
                f"Longitude: {self.longitude}")


def get_coordinates() -> Coordinates:
    ...
    return Coordinates(20, 30)


if __name__ == '__main__':
    c = get_coordinates()
    # c.longitude = 100
    print(c)
