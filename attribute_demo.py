class Foo:
    name = 'Foo class attribute'

    def fn(self):
        pass


# __dict__: A dictionary or other mapping object used to store an object’s (writable) attributes.
print('class attribute:', Foo.__dict__)

foo = Foo()

# use builtin method hasattr(), setattr() and getattr() to access attribute of a instance
print(hasattr(foo, 'name'))
setattr(foo, 'name', 'Nicole')
print(getattr(foo, 'name'))

foo.__setattr__('name', 'foo instance attribute')
print(foo.__getattribute__('name'))

foo.name = 'foo instance attribute'
print('instance attribute:', foo.__dict__)
