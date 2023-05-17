"""Module with functions checking with assert"""
from main_module import Student
from generator import Generator


class TestGeneratorClass:
    """Class to check out function in Generator class"""
    def test_generate_single(self):
        """Method checking - generate_single()"""
        generator = Generator()
        student = generator.generate_single()
        assert isinstance(student, Student)

    def test_one_thousand_generator(self):
        """Method checking - one_thousand_generator()"""
        generator = Generator()
        students = generator.one_thousand_generator()
        assert isinstance(students, list)
        assert len(students) == 1000

    def test_ten_thousand_generator(self):
        """Method checking -  ten_thousand_generator()"""
        generator = Generator()
        students = generator.ten_thousand_generator()
        assert isinstance(students, list)
        assert len(students) == 10000
