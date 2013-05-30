#
# median.py
#

from sys import argv

nums = argv[1:]

if len(nums) % 2 == 0:
    median = (float(nums[len(nums)/2]) + float(nums[len(nums)/2 - 1]))/2
else:
    median = nums[len(nums)/2]

print median
    
