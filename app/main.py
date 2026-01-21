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

def write_students_information(students: list[Student]) -> int:
    students_num = 0
    with open("student.pickle", "wb") as f:
        for student in students:
            students_num += 1
            pickle.dump(student, f)
    return students_num

def read_groups_information(groups_file: str) -> set:
    specialties = []
    with open(groups_file, "rb") as f:
        groups = f.readlines(f)
        for group in groups:
            specialties.append(pickle.loads(group).speciality)
    return set(specialties)

def read_students_information(students_file: str) -> set:
    students_list = []
    with open(students_file, "rb") as f:
        students = f.readlines(f)
        for student in students:
            students_list.append(pickle.loads(student))
    return students_list
