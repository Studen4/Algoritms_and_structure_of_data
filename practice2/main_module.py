"""Module for create generator of data"""


class Student:
    """All methods which needs personally to students"""
    name: str  # student name
    surname: str  # student surname
    discipline: str  # name of discipline
    mark: int  # exams mark
    exam: str = "exam"  # const variable

    def __init__(self, name: str, surname: str,
                 discipline: str, mark: int, exam: str = "exam") -> None:
        """Constructor of the class to set up all basic variables"""
        self.name = name
        self.surname = surname
        self.discipline = discipline
        self.mark = mark
        self.exam = exam

    def get_info(self) -> str:
        """String representation of the object"""
        return f"Student({self.name}, {self.surname}, {self.discipline}, {self.exam}, {self.mark})"

    def __repr__(self) -> str:
        """String representation of the object"""
        return f"Student({self.name}, {self.surname}, {self.discipline}, {self.exam}, {self.mark})"
