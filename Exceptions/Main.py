# Исключения

# <editor-fold desc="Part 1">

# def divide(num1, num2):
#     return num1 / num2
#
#
# try:
#     print(divide(4, 0))
# except:
#     print("Something went wrong...")

# </editor-fold>


# <editor-fold desc="Part 2">

# def foo(num1, num2):
#     if num2 == 0:
#         raise ZeroDivisionError
#     if num1 != int(num1) or num2 != int(num2):
#         raise TypeError
#
#
# try:
#     foo(4, '4')
# except ZeroDivisionError:
#     print("Division to zero error")
# except TypeError:
#     print("Arguments must be int")

# </editor-fold>


# <editor-fold desc="Part 3">

# import MyExceptions
#
#
# def foo(num1, num2):
#     if num2 == 0:
#         raise ZeroDivisionError
#     if num1 != int(num1) or num2 != int(num2):
#         raise MyExceptions.ArgumentTypeError("Argument must be int", 202)
#
#
# try:
#     foo(4, '4')
# except ZeroDivisionError:
#     print("Division to zero error")
# except MyExceptions.ArgumentTypeError as ex:
#     print(ex.message, "Code: ", ex.code)


# </editor-fold>


# <editor-fold desc="Part 4">
# import MyExceptions
#
#
# class MyCol:
#     def __init__(self, *args):
#         self.items = list(args)
#
#     def __getitem__(self, item):
#         if item >= len(self.items):
#             raise MyExceptions.OutOfRangeError("Index out of range", item - len(self.items) + 1)
#         else:
#             return self.items[item]


# nums = MyCol(1, 2, 3, 4, 5)
# try:
#     print(nums[3])
# except MyExceptions.OutOfRangeError as er:
#     print(er.message, er.code)

# </editor-fold>
