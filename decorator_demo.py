"""
First-Class Objects
In Python, functions are first-class objects. This means that functions can be passed around and used as arguments, just
like any other object (string, int, float, list, and so on).

Inner Functions
It’s possible to define functions inside other functions. Such functions are called inner functions.
"""


def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()


parent()

"""
Returning Functions From Functions
Python also allows you to use functions as return values. The following example returns one of the inner functions 
from the outer parent() function
"""


# def parent(num):
#     def first_child():
#         return "Hi, I am Emma"
#
#     def second_child():
#         return "Call me Liam"
#
#     if num == 1:
#         return first_child
#     else:
#         return second_child
#
#
# print(parent(1)())
# print(parent(2)())

"""
Simple Decorators
Now that you’ve seen that functions are just like any other object in Python, you’re ready to move on and see the 
magical beast that is the Python decorator

Put simply: decorators wrap a function, modifying its behavior.
"""

# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#
#     return wrapper
#
#
# def say_whee():
#     print("Whee!")
#
#
# say_whee = my_decorator(say_whee)
# say_whee()

"""
Syntactic Sugar!
The way you decorated say_whee() above is a little clunky. First of all, you end up typing the name say_whee three times
In addition, the decoration gets a bit hidden away below the definition of the function.

Instead, Python allows you to use decorators in a simpler way with the @ symbol, sometimes called the “pie” syntax. 
The following example does the exact same thing as the first decorator example:
"""

# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#
#     return wrapper
#
#
# @my_decorator
# def say_whee():
#     print("Whee!")
#
# say_whee()


"""
Decorating Functions With Arguments

The problem is that the inner function wrapper() does not take any arguments, but name="Jeremy" was passed to it.

"""


# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#
#     return wrapper
#
#
# @my_decorator
# def say_whee(name):
#     print(name)
#
#
# say_whee('Jeremy')

# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Something is happening before the function is called.")
#         func(*args, **kwargs)
#         print("Something is happening after the function is called.")
#
#     return wrapper
#
#
# @my_decorator
# def say_whee(*args, **kwargs):
#     print([arg for arg in args])
#     print([kwargs[kwarg] for kwarg in kwargs])
#
#
# say_whee('Jeremy', 'Joe', age=18, class_name='Python')
