"""If-elif-else.

#given values w,x,y,z
#write if-elif-else statement that will
search minimum value and print smth aka "'y' is minimum value'
#where 'y' is variable name (not value)
#advice use python debugger and different values to check your algorithm
#optionally you can check your algorithm somehow with assert statements
w, x, y, z = 100, 200, 40, 300
"""

w, x, y, z = 100, 200, 40, 300

"""
Checking the number is the smallest.
"""

if (x < w) and (x < y) and (x < z):
    print('x is minimum value')
elif (y <= w) and (y <= x) and (y <= z):
    print('y is minimum value')
elif (w < x) and (w < y) and (w < z):
    print('w is minimum value')
else:
    print('z is minimum value')