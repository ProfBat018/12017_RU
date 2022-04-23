import string
import random

# <editor-fold desc="Вартианты импортов">

# <editor-fold desc="Example 1. Мой любимый вариант">

# import random
# import MyLib
#
# random.choice()
# MyLib.choice()

# </editor-fold>

# <editor-fold desc="Example 2. Не самый лучший способ">

# import random as r
# import MyLib as M
#
# r.choice()
# M.choice()

# </editor-fold>

# <editor-fold desc="Example 3. Никогда так не делайте (⊙_⊙;)">
# * - значит импоритровать все функции из модуля

# from random import *
# from MyLib import *

# choice()

# </editor-fold>

# <editor-fold desc="Example 4. Неплохая альтернатива, если названия не совпадают и нам нужон взять мало функций">

# from random import choice, randint
# from MyLib import choice

# </editor-fold>

# </editor-fold>

# <editor-fold desc="Вариант 1, с буквами вручную">

# lower_letters = 'qwertyuiopasdfghjklzxcvbnm'
# upper_letters = lower_letters.upper()
#
# print(upper_letters)

# </editor-fold>

# <editor-fold desc="Вариант 2, с буквами автоматически">

# lower_letters = str()
# upper_letters = str()
#
# i = 97
# while i <= 122:
#     lower_letters += chr(i)
#     upper_letters += chr(i).upper()
#     i += 1

# </editor-fold>

# <editor-fold desc="Вариант 3, Для мега ленивых людей, то есть для вас )) ">


def check_choice(choice: int, result_list: list):
    if result_list.__contains__(choice):
        print("You already selected this item...")
        return False
    if choice == 5:
        if result_list.__contains__(1) or result_list.__contains__(2):
            return True
        else:
            print("You must select first or second item")
            return False
    elif 1 <= choice < 5:
        return True


def select_password():
    choice_result = list()

    while True:
        choice = int(input("Enter your choice: \n"
                           "1. Lower letters\n"
                           "2. Upper letters\n"
                           "3. Digits\n"
                           "4. Symbols\n"
                           "5. Exit\n"))

        check_result = check_choice(choice, choice_result)
        if check_result and choice == 5:
            break
        elif check_result:
            choice_result.append(choice)

    return choice_result


lower_letters = string.ascii_lowercase
upper_letters = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation
password = str()

result = select_password()
components = [lower_letters, upper_letters, digits, symbols]

length = int(input("Enter length of your password"))

for i in range(length):
    template = str()
    for item in result:
        template += random.choice(components[item - 1])
    password += random.choice(template)

print(password)


# </editor-fold>
