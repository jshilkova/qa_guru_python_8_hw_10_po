import dataclasses
import enum
from datetime import datetime


class Hobby(enum.Enum):
    sports = "Sports"
    reading = "Reading"
    music = "Music"


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile: str
    date_of_birth: datetime.date
    subjects: list[str]
    hobbies: list[str]
    picture: str
    address: str
    state: str
    city: str


@dataclasses.dataclass
class SimpleUser:
    full_name: str
    email: str
    current_address: str
    permanent_address: str
