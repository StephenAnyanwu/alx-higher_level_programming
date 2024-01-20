#!/usr/bin/python3

"""
Defines a class Student
"""


class Student:
    """
    Impliment a student

    Attributes
    ----------
    first_name : str
        student's first name
    last_name : str
        student's last name
    age : int
        student's age

    Methods
    -------
    to_json()
        retrieves a dictionary representation
        of a Student instance
    """
    def __init__(self, first_name, last_name, age):
        """
        Parameters
        ----------
        first_name : str
            student's first name
        last_name : str
            student's last name
        age : int
            student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        retrieves a dictionary representation
        of a Student instance

        Returns
        -------
        dict
            dictionary representation
            of a Student instance
        """
        return self.__dict__


if __name__ == "__main__":
    student = Student("Steve", "Anyanwu", 28)
    print(student.to_json())

    students = [
                Student("John", "Doe", 23),
                Student("Bob", "Dylan", 27)
            ]

    for student in students:
        j_student = student.to_json()
        print(type(j_student))
        print(j_student['first_name'])
        print(type(j_student['first_name']))
        print(j_student['age'])
        print(type(j_student['age']))
