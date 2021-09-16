# def power1(a, b=4):
#     if type(a)==int and type(b)==int:
#         return a**b
#
#
# print(power1(2))
# print(power1(2.5,5))

# list1 = list(range(20))
# print(list1)
# # list2=[]
# # for num in list1:
# #     if num>10:
# #         list2.append(num)
#
# list2=[num for num in list1 if num>10]
#
# print(list2)


# data = '3, 5, 7, 9, 11'
#
# num_list=list(map(int, data.split(', ')))
# print(num_list)
# num_tuple=tuple(num_list)
# print(num_tuple)

# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]
#
# list3 =zip(list1, list2)
# print(list3)
# for el in list3:
#     print(f'{el[0]} {el[1]}')

# def func1(param1, param2):
#     return param1 < param2
#
#
# def loop(times, func):
#     for i in range(times):
#         if func(i, 10):
#             break
#
# # loop(10, func1)
# from datetime import date,datetime
#
# print(datetime.today())

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age: int = age
#
#     @staticmethod
#     def comare(p1, p2):
#         return p1.age > p2.age
#         # if p1.age > p2.age:
#         #     return True
#         # return Fals
#
# person1 = Person('Peter', 15)
# person2 = Person('Ivan', 23)
#
# print(Person.comare(person1, person2))

# def positives(num):
#     for i in range(num):
#         yield i
#
# first_five = positives(6)
# for i in first_five:
#     print(i)

def positives():
    num = 1
    yield num
    num +=1

first_five = positives()
for i in range(1, 6):
    print(i)

# SELECT * FROM Employee , Department
# JOIN Employee.department_id ,