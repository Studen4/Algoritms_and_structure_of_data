"""Module to create generator for students"""

import random
import names
from main_module import Student


class Generator:
    """Class to generate objects of Student"""
    disciplines = (
        "Algorithms and Data Structures",
        "Fundamentals of Programming",
        "Databases",
        "Information Security",
        "Fundamentals of Machine Learning",
        "Linux Administration"
    )
    exam = ["exam", "credit", "differential credit"]

    @staticmethod
    def generate_single() -> Student:
        """Method for generating a single Student object with random values"""
        name = names.get_first_name()
        surname = names.get_last_name()
        exam = random.choice(Generator.exam)
        discipline = random.choice(Generator.disciplines)
        mark = random.randint(0, 100)
        return Student(name, surname, discipline, mark, exam)

    def one_thousand_generator(self) -> list:
        """Method for generating a list of 1000 Student objects"""
        students = []
        for _ in range(1000):
            student = self.generate_single()
            students.append(student)
        return students

    def ten_thousand_generator(self) -> list:
        """Method for generating a list of 10000 Student objects"""
        students = []
        for _ in range(10000):
            student = self.generate_single()
            students.append(student)
        return students


if __name__ == "__main__":
    generator = Generator()

    st = generator.generate_single()
    print(st)

    students_1000 = generator.one_thousand_generator()
    print(len(students_1000))

    students_10000 = generator.ten_thousand_generator()
    print(len(students_10000))
