# <editor-fold desc="Happy number">


# number = int(input())
# division = 1
#
# i = number
# count = 0
# lsum = 0
# rsum = 0
#
# while count != 6:
#     i = number // division
#     digit = i % 10
#     division *= 10
#     if count < 3:
#         rsum += digit
#     elif count >= 3:
#         lsum += digit
#     count += 1
#
# print(lsum)
# print(rsum)
# if lsum == rsum:
#     print("Happy")
# else:
#     print("No")
# </editor-fold>

# <editor-fold desc="While else">

num1 = 1
num2 = 10

i = num1

check = True

while check:
    print(i)
    i += 1
    if i == num2:
        check = False
else:
    print("Числа закончились")

# </editor-fold>
