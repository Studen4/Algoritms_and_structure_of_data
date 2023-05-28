"""Module with search-by tree realisation."""
from tree_bonus_algorithm import AbstractTreeBonus


class Person:
    """Class representing a person."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

    def __lt__(self, other):
        """Less than comparison for Person objects."""
        return self.age < other.age


class AbstractTreeSearchBy(AbstractTreeBonus):
    """Class with search-by modification for a tree."""

    def find_by(self, attribute, value):
        """
        Performs a search for elements by a class attribute.
        Arguments:
            attribute: The name of the attribute to search by.
            value: The value of the attribute to search for.
        Returns:
            A list of found elements that satisfy the search criteria.
        """
        found_value = filter(lambda x: getattr(x, attribute) == value, self)
        return list(found_value)

    def create_person(self, name, age):
        """
        Creates a Person object and inserts it into the tree.
        Arguments:
            name: The name of the person.
            age: The age of the person.
        """
        person = Person(name=name, age=age)
        self.insert(person)


if __name__ == "__main__":
    # Create an instance of the tree
    tree = AbstractTreeSearchBy()

    # Insert elements into the tree
    tree.create_person("John", 25)
    tree.create_person("Jane", 30)
    tree.create_person("Alice", 22)
    tree.create_person("Bob", 35)

    # Perform attribute-based search
    found = tree.find_by("age", 30)
    print("Results of search:")
    for item in found:
        print(item)
