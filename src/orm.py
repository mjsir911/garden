#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import sqlite3

__appname__     = ""
__author__      = "Marco Sirabella"
__copyright__   = ""
__credits__     = ["Marco Sirabella"]  # Authors and bug reporters
__license__     = "GPL"
__version__     = "1.0"
__maintainers__ = "Marco Sirabella"
__email__       = "msirabel@gmail.com"
__status__      = "Prototype"  # "Prototype", "Development" or "Production"
__module__      = ""

class Object():
    """

    >>> error = Object()
    Traceback (most recent call last):
        ...
    TypeError: Can't instantiate abstract class Object
    >>> class Person(Object):
    ...     columns = {'age': int, 'name': str}
    >>> martin = Person(name='martin', age=17)
    >>> cols = martin.__dict__
    >>> print(cols.items())
    dict_items([('name', 'martin'), ('age', 17)])

    """
    colums = {}
    def __new__(cls, *args, **kwargs):
        if cls.__bases__[0] is object: raise TypeError("Can't instantiate abstract class {}".format(cls.__name__))
        return super().__new__(cls)

    def __init__(self, **kwargs):
        assert self.columns.keys() == kwargs.keys()
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __del__(self):
        print('deleted')

    @classmethod
    def load(cls, db, table, ident):
        #load db
        #load table
        #return class matching ident
        pass


def table(obj):
    pass


def add(obj):
    sqlite3.execute('''
    INSERT INTO {} VALUES (?)
    '''.format(type(obj).__name__), obj.__dict__)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
