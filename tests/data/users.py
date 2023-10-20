import dataclasses

@dataclasses.dataclass
class DateOfBirth:
    day: str
    month: str
    year: str

@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile: str
    date_of_birth: DateOfBirth
    subjects: list[str]
    hobbies: list[str]
    picture: str
    address: str
    state: str
    city: str




