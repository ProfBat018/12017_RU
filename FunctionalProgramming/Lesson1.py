# Functional Programming
import functools

# <editor-fold desc="Map">

# <editor-fold desc="Without">

# def find_even(collection: list):
#     result = list()
#     for item in collection:
#         if item % 2 == 0:
#             result.append(item)
#
#     return result
#
#
# nums = [i for i in range(1, 101)]
#
# even_nums = find_even(nums)
# print(even_nums)

# </editor-fold>

# <editor-fold desc="With Map">

# <editor-fold desc="Example 1">
#
# def find_even(num):
#     if num % 2 == 0:
#         return num
#
#
# nums = [i for i in range(1, 101)]
#
# even_result = list(map(find_even, nums))
# print(even_result)

# </editor-fold>

# <editor-fold desc="Example 2">

# def add(num):
#     return num + 10
#
#
# nums = [i for i in range(1, 101)]
#
# result = tuple(map(add, nums))
# print(result)

# </editor-fold>

# <editor-fold desc="Example 3">

# lambda - это анонимная функция. То есть, функция у которого нет названия.

# nums = [i for i in range(1, 101)]
#
# result = list(map(lambda num: num + 10, nums))

# print(result)



# </editor-fold>

# </editor-fold>

# </editor-fold>

# <editor-fold desc="Reduce">


# nums = [i for i in range(1, 101)]
# res2 = functools.reduce(lambda a, b: a + b, nums)
# print(res2)


# </editor-fold>

# <editor-fold desc="Filter">

# nums = [i for i in range(1, 101)]
#
# nums = list(map(lambda x: x % 2 == 0, nums))
# nums = list(filter(lambda x: x % 2 == 0, nums))
#
# print(nums)

# </editor-fold>
