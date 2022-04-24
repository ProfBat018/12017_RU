import random

nums = set()

for i in range(10):
    nums.add(random.randint(1, 10))

tmp = {12, -5, 14, 10}

# nums = nums.union(tmp)

# print(nums.difference(tmp))
# print(nums.intersection(tmp))

# print(nums)
# nums.difference_update(tmp)
# print(nums)

print(nums)
print(tmp)
print(nums.symmetric_difference(tmp))


