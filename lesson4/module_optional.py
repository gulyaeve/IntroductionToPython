from dataclasses import dataclass
from typing import Optional, Union


@dataclass
class User:
    id: int
    name: str
    address: Union[str, dict, int]
    address2: str | None
    job: Optional[str, dict] = None

