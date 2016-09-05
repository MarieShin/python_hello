"""
--> docstring
hello.py
author : marie
date : 20160905
"""
print('hello.world')

a = 3
b = 'hello'

print(str(a) + b)

my_str = "Hello my name is Marie Shin. you can call me Shin"

my_str_list = my_str.split(' ')[5]

my_name = my_str.split(' ')[5][:-1]

print(my_name)

print(my_str[23:-22])

# from datetime import datetime
#
# my_time = datetime.datetime.now()
#
# print(my_time)


import math


# print(math.sqrt(13689))


def distance_from_zero(distance):
    if type(distance) == int or type(distance) == float:
        return math.fabs(distance)
    else:
        return 'Nope'


print(int(distance_from_zero(-4560)))


def param_test(first_number, second_number):
    return first_number + (second_number * 2)


print(param_test(second_number=5, first_number=6))


def var_param_test(*p):
    # print(p)
    # print(type(list(p)))

    for item in p:
        print(item)


var_param_test(1, 2, 3, 4, 5)


def double_return():
    return 3, 4, 5


result = double_return()

print(type(result), result)

result1 = (lambda x, y: x * y)(3, 4)

print(result1)

import calculator

print(calculator.add(3, 5))
print(calculator.sub(5, 3))


import sys

path_list = sys.path

for item in path_list:
    print(item)


inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
# inventory['burlap bag'] = ['apple', 'small ruby', 'three-toe aloth']

# Sorting the list found under the key 'pouch'
# inventory['pouch'].sort()

# Your code here
inventory['pocket'] = ['seashell', 'strange berry', 'lint']

inventory['backpack'].sort()

inventory['backpack'].remove('dagger')

inventory['gold'] += 50
print(inventory)