# def add(num1, num2):
#     return num1 + num2
#
#
# num1 = 1
# num2 = 2
#
# result = add(num1, num2)
# print(result)


def add(numbers: tuple):
    addition = 0
    for number in numbers:
        addition += number
    return addition


nums = list()
while True:
    tmp = int(input("Enter number: 0 for exit"))
    if tmp:
        nums.append(tmp)
    else:
        break


nums = tuple(nums)
print(add(nums))
