from dataclasses import dataclass
from datetime import datetime
import pickle


@dataclass
class Speciality:
    name: str
    number: int

@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str

@dataclass
class Group:
    speciality: Speciality
    course: str
    students: list[Student]

def write_groups_information(groups: list[Group]) -> int:
    max_students = 0
    with open("group.pickle", "wb") as f:
        for group in groups:
            if len(group.students) > max_students:
                max_students = len(group.students)
            pickle.dump(group, f)

    return max_students

