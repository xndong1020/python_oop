class Student:
    count = 0

    def enroll(self):
        Student.count += 1


student1 = Student()
student1.enroll()

print(Student.count)

student2 = Student()
student2.enroll()

print(Student.count)

print(Student.__dict__)
print(student1.__dict__)

# class Student:
#
#     def __init__(self, age):
#         self.age = age
#
#     def __str__(self):
#         return str(self.age)
#
#     def __call__(self, *args, **kwargs):
#         print(self)
#
#
# student1 = Student(18)
# student1()
#
# student2 = Student(28)
# student2()
#
# print(Student.__dict__)
# print(student1.__dict__)
