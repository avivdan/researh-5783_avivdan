# import constraint as csp
import random
import doctest
import pytest


class Student:
    def __init__(self, name: str, budget: float, preferences: list,year: int = 1, courses: list= []) -> None:
        self.name = name
        self.budget = budget
        self.courses = courses
        self.preferences = preferences


class Course:
    def __init__(self, name: str, price: float, max_capacity: int,  capacity: int=0) -> None:
        self.name = name
        self.price = price
        self.capacity = capacity
        self.max_capacity = max_capacity


a = Course(name = 'a', price = 12, max_capacity=5)
b = Course(name = 'b', price = 2, max_capacity=3)
c = Course(name = 'c', price = 4.5, max_capacity=5)
courses = [a,b,c]



s1 = Student(name = 's1', budget=15, preferences=([c,b]))
s2 = Student(name = 's2', budget=15, preferences=([b,c,a]))
s3 = Student(name = 's3', budget=15, preferences=([b,a]))
s4 = Student(name = 's4', budget=15, preferences=([a,c]))
s5 = Student(name = 's5', budget=15, preferences=([a,b,c]))
students = [s1,s2,s3,s4,s5]


# def sort_oversubscribtion(course_list:list)->list:
#     '''
#     sort function for sorting the must oversubscribed course
#     '''
#     def compare(a:Course, b:Course):
#         return (a.capacity - a.max_capacity) - (b.capacity - b.max_capacity)
#     return sorted(course_list, cmp = compare)




a = Course(name='a', price=6, capacity=0, max_capacity=3)
b = Course(name='b', price=4, capacity=0, max_capacity=3)
c = Course(name='c', price=6, capacity=0, max_capacity=3)
courses = [a, b, c]


s1 = Student(name='s1', budget=10, courses=[], preferences=([a]))
s2 = Student(name='s2', budget=10, courses=[], preferences=([b,a]))
s3 = Student(name='s3', budget=10, courses=[], preferences=([c]))
s4 = Student(name='s4', budget=10, courses=[], preferences=([c,b]))
s5 = Student(name='s5', budget=10, courses=[], preferences=([c, a, b]))

students = [s1, s2, s3, s4, s5]


def mapping_csp(students: list, courses: list) -> dict:
    def get_course(s: Student) -> bool:
        for i in range(0, len(s.preferences)):
            if (s.budget >= s.preferences[i].price):
                s.courses.append(s.preferences[i])
                s.budget = s.budget - s.preferences[i].price
                s.preferences[i].capacity += 1
                s.preferences.pop(i)
                return True
        return False
    while True:
        flag = False
        for student in students:
            if (len(student.preferences) > 0):
                if (get_course(student)):
                    flag = True
        if (not flag):
            break
    # return {course.name: course.capacity for course in courses}
    for student in students : print("{0} and {1}".format(student.name,student.budget))
    return {student.name: student.courses for student in students}

a = mapping_csp(students=students, courses=courses)
# print(a)


# (2.4,5,10.4)
for student in a:
    print(student)
    # print(student.budget)
    for course in a.get(student):
        print(course.name   )
    print("*******************************")

# # def get_course(s:Student)->bool:
# #     for i in range(0,len(s.preferences)):
# #        if(s.budget >= s.preferences[i].price):
# #             s.courses.append(s.preferences[i])
# #             s.budget = s.budget - s.preferences[i].price
# #             s.preferences[i].capacity += 1
# #             s.preferences.pop(i)
# #             return True
# #     return False





# while True:
#     flag = False
#     for student in students:
#         if(len(student.preferences) > 0):
#             if(get_course(student)):
#                flag = True
#     if(not flag):
#         break


# for course in courses:
#     print("course name is {0} and in capacity of {1}".format(course.name, course.capacity))


# # for student in students:
# #     print(student.name, ":")
# #     for course in student.courses:
# #         print(course.name)
# #     print("****************************")

# #what do we wANt
# # we need to create constraint problem to course allocation
# # what the csp stands for - does the budget will be suefficent
# # for the courses


# def algorithm1(max_budget:int, map_price_demand:function, sort_alpha:function, time:float) -> list:
#     pass


# def sort_function(students_list:list)->list:
#     def compare(a:Student, b:Student):
#         if(a.year - b.year == 0):
#             return a.budget - b.budget
#         return a.year - b.year
#     return sorted(students_list, cmp = compare)

# def sort_oversubscribtion(course_list:list)->list:
#     def compare(a:Course, b:Course):
#         return (a.capacity - a.max_capacity) - (b.capacity - b.max_capacity)
#     return sorted(course_list, cmp = compare)



# a = [[0,1,1],
#      [0,1,1],
#      [1,1,0],
#      [1,0,1],
#      [1,1,0]]
