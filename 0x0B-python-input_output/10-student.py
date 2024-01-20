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
    to_json(attrs=None)
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

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation
        of a Student instance

        Parameters
        ----------
        attrs : list
             a list of strings, only attribute names
             contained in this list must be retrieved
        Returns
        -------
        dict
            dictionary representation
            of a Student instance
        """
        if attrs is None:
            return self.__dict__
        selected_attrs = {k: v for k, v in self.__dict__.items() if k in attrs}
        return selected_attrs


if __name__ == "__main__":
    student_1 = Student("John", "Doe", 23)
    student_2 = Student("Bob", "Dylan", 27)

    j_student_1 = student_1.to_json()
    j_student_2 = student_2.to_json(['first_name', 'age'])
    j_student_3 = student_2.to_json(['middle_name', 'age'])

    print(j_student_1)
    print(j_student_2)
    print(j_student_3)
