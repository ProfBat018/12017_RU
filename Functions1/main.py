# def print_hello():
#     print("Hello World")
#
#
# def add(num1, num2):
#     return num1 + num2
#
#
#
# result = add(5, 6)
# print(result)
# print(add(1, 2))


# def even(number: int):
#     return number % 2 == 0
#
#
# print(even(2))

# def addition(*nums):
#     result = 0
#     for number in nums:
#         result += number
#     return result
#
#
# print(addition(1, 2, 3, 4, 56, 7, 8, 9, 6, 4, 2, 23))


# def foo2(*args, name, surname):
#     print(name, surname, args)
#
#
# foo2(1, 2, 4, 5, 6, 7, 8, name="Elvin", surname="Azimov")


# def foo3(num1, num2, num3=5):   # default parameter
#     print(num1 + num2 + num3)
#
#
# foo3(1, 2, 3)


def foo4(num1, num3):
    return num1, num3


print(foo4(1, 2))

a = list(foo4(1, 2))
