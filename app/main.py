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