import logging


class LoggerMixin:
    @property
    def logger(self):
        name = '.'.join([
            self.__module__,
            self.__class__.__name__
        ])
        logging.basicConfig(level=logging.DEBUG)
        return logging.getLogger(name)


class Person:

    def __init__(self, name):
        self.name = name


class Student(LoggerMixin, Person):

    def __init__(self, name):
        self.name = name
        self.logger.warning('Logger from mixins is working...')


student = Student('Jeremy')
print(isinstance(student, Student))
print(isinstance(student, LoggerMixin))
