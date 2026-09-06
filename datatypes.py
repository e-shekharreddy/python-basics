# datatypes and varables in python 
# types of comment in python
# 1. single line comments
# 2. Inline comments
# 3. Block comments

# this is my integer : single line comment
my_int = 108 # value 108 is store in my_int container : Inline cpmment
print(my_int)

'''
we can write blocked comments like this 
'''

"""
we can write blocked comments like this in triple '''
"""

my_float =  10.25563
print(my_float)

my_bool = True # False
print(my_bool)
# python is case sensitive

my_str = "sample string"



# operstions : +, -, /, *

first_num = 10
second_num = 30

add = first_num + second_num
sub = second_num - first_num
div = second_num / first_num
multi = first_num * second_num

print(add, sub, div, multi, sep="\n", end="***") 
print(add, sub, div, multi)

# lets see type
print(type(div))

# // -> integer division
quotient = second_num // first_num
print(quotient, type(quotient))


#  % -> modulo operator
reminder = second_num % first_num
print(reminder, type(reminder))