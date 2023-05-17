"""Module with functions checking with assert"""
from main_module import Student


class TestStudentClass:
    """Class to make test for Student"""
    def test_data_type(self):
        """Check validation of Student class"""
        student = Student("Name", "Surname", "Discipline", 87)
        assert isinstance(student, Student)

    def test_check_init(self):
        """Init and appending data - checking"""
        student = Student("Name", "Surname", "Discipline", 87)
        assert student.name == "Name"
        assert student.surname == "Surname"
        assert student.discipline == "Discipline"
        assert student.mark == 87

    def test_check_default(self):
        """Method checking - basic variables"""
        student = Student("Name", "Surname", "Discipline", 87)
        assert student.exam == "exam"

    def test_get_info(self):
        """Method checking - get_info()"""
        student = Student("Name", "Surname", "Discipline", 87)
        info = student.get_info()
        assert isinstance(info, str)
        assert "Name" in info
        assert "Surname" in info
        assert "Discipline" in info
        assert "87" in info

    def test_repr(self):
        """Method checking - __repr__()"""
        student = Student("Name", "Surname", "Discipline", 87)
        repr_str = repr(student)
        assert isinstance(repr_str, str)
        assert "Name" in repr_str
        assert "Surname" in repr_str
        assert "Discipline" in repr_str
        assert "exam" in repr_str
        assert "87" in repr_str
