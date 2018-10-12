class Person:

    def __init__(self, name, class_name):
        self.name = name
        self._class_name = class_name

    @property
    def class_name(self):
        return self._class_name

    @class_name.setter
    def class_name(self, value):
        if not value:
            raise ValueError('Please provide a valid class name')
        self.__dict__['_class_name'] = value


person = Person('Jeremy', 'Python')

print(person.name)
print(person.class_name)

person.name = 'Zhang'
person.class_name = '.Net'
print(person.name)
print(person.class_name)


