#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """ Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize student props in contructor
        Args:
            first_name (str): The first name of student.
            last_name (str): The last name of student.
            age (int): The age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
