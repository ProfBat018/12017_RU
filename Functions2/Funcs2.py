# task1


# def multi(numbers: tuple):
#     addition = 1
#     for number in numbers:
#         addition *= number
#     return addition
#
#
# nums = list()
# while True:
#     tmp = int(input("Enter number: 0 for exit: "))
#     if tmp:
#         nums.append(tmp)
#     else:
#         break
#
#
# nums = tuple(nums)
# print(multi(nums))

# task2
#
# def mins(numbers: tuple):
#     addition = 0
#     for number in numbers:
#         addition = numbers[0]
#         if addition < number:
#             addition = number
#         elif addition > number:
#             addition = number
#         else:
#             addition = addition
#     return addition
#
#
# nums = list()
# while True:
#     tmp = int(input("Enter number: 0 for exit: "))
#     if tmp:
#         nums.append(tmp)
#     else:
#         break
#
#
# nums = tuple(nums)
# print(mins(nums))


# task3
#
# def pro(numbers: tuple):
#     addition = 0
#     for number in numbers:
#         if number == 3 or number == 5 or number == 7 or number != 1 and number % 3 != 0 and number % 2 != 0 and number % 5 != 0:
#             addition += 1
#     return addition
#
#
# nums = list()
# while True:
#     tmp = int(input("Enter number: 0 for exit: "))
#     if tmp:
#         nums.append(tmp)
#     else:
#         break
#
#
# nums = tuple(nums)
# print(pro(nums))

# task4


# def delet(numbers: tuple):
#     addition = list()
#     for number in numbers:
#         if number != tmp2:
#             addition.append(number)
#     return addition
#
#
# nums = list()
# while True:
#     tmp = int(input("Enter number: 0 for exit: "))
#     if tmp:
#         nums.append(tmp)
#     else:
#         break
# tmp2 = int(input("Enter delete: 0 for exit: "))
#
# nums = tuple(nums)
# print(delet(nums))

# task5


# def two_list(numbers1: tuple, numbers2: tuple):
#     result = list()
#     for number in numbers1:
#         result.append(number)
#     for number in numbers2:
#         result.append(number)
#
#     return result
#
#
# nums1 = [1, 2, 3, 4, 5]
# nums2 = [3, 4, 3, 5, 6, 7]
# while True:
#     tmp = int(input("Enter number: 0 for exit: "))
#     if tmp:
#         nums1.append(tmp)
#     else:
#         break
#
# while True:
#     tmp2 = int(input("Enter number2: 0 for exit: "))
#     if tmp2:
#         nums2.append(tmp2)
#     else:
#         break

# print(two_list(tuple(nums1), tuple(nums2)))

# task6

# def stepen(numbers: tuple, power: int):
#     addition = list()
#
#     for number in numbers:
#         number = (number**power)
#         addition.append(number)
#     return addition
#
#
# nums = list()
# while True:
#     tmp = int(input("Enter number: 0 for exit: "))
#     if tmp:
#         nums.append(tmp)
#     else:
#         break
# tmp2 = int(input("Enter stepen : "))
#
# nums = tuple(nums)
#
# print(stepen(nums, tmp2))


# def fact(num):
#     if num == 1:
#         return 1
#     return num * fact(num - 1)
#
#
# print(fact(5))


# def nod(num1, num2):
#     while num1 != num2:
#         if num1 > num2:
#             return nod(num1 - num2, num2)
#         else:
#             return nod(num1, num2 - num1)
#     return num1
#
#
# def nod2(num1, num2):
#     division = 0
#     result = 0
#
#     while division <= num1 or division <= num2:
#         division += 1
#         if num1 % division == 0 and num2 % division == 0:
#             result = division
#     print(result)
#
#
# first_num = 24
# second_num = 16
#
#
# print(nod2(first_num, second_num))

# import random
#
# name = "Elvin"
# nums = [i for i in range(1, 11)]
#
# num = random.randint(1, 10)
# print(random.choice(name))

# a = random.randint(0, len(name) - 1)
# print(name[a])

# from random import randint
import random as r

name = "Elvin"
nums = [i for i in range(1, 11)]

num = r.randint(1, 10)
