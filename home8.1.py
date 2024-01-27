"""Generating  multiplication table.

# Given 0 < number (integer) <= 11
# You need to print multiplication table based on this number
#
# Example: num=5
# Output:
#  1   2   3   4   5
#  2   4   6   8  10
#  3   6   9  12  15
#  4   8  12  16  20
#  5  10  15  20  25
"""
num = 5

newlist = [[x*y for x in range(1, num + 1)] for y in range(1, num + 1)]

print(newlist)