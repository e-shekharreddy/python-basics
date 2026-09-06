# string datatype
# a string cnsists ofcharectors
sample_str = "welcome to my git"

# a string is am array of charecters 
# How to access individual elements in an array ?
# python is zero index based and -ve index based

first_char = sample_str[0]
# print(first_char)
last_char = sample_str[-1]
# print(last_char)

str_len = len(sample_str)
# print(str_len)

words = sample_str.split(sep=" ")
# print(words, type(words))

# print(dir(sample_str))


"""
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', 
'__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', 
'__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__',
 '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
 '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 
 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier',
'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower',
'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex',
'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 
'title', 'translate', 'upper', 'zfill']
"""

sample_str = " hello welcome to python "
# print(sample_str.strip())

sample_str = "welcome back to git"

# how to extract first 2 characters of sample_str
# To do this weuse ':' operator
# Usage: start:end:step, all three are not mandatory
# Importent : end index is not included so we have to add +1 then only we get what we want

first_two = sample_str[0:7]  # here the step size vaue is 1 (default)
print(first_two)

alternate_chars = sample_str[::2] # stat:0 end: len(str) these are default values
print(alternate_chars)

# *** Reverse a string *** 
reverse_string = sample_str[::-1] # start:len(str), end:0, step: -1
print(reverse_string)