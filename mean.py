#
# mean.py
#

from sys import argv

nums = argv[1:]

for index, value in enumerate(nums):
    nums[index] = float(value)

mean = sum(nums)/len(nums)

print mean
