my_dict = {} # dirc ()
print(type(my_dict))

# a dictonary consists of key-value pairs
my_dict = {"a": 1, "b": 3, 3: True}
print(my_dict)


# my_dict = {"a": 1, "b": 3, 3: True, ['a','c']: 123} 
# print(my_dict) # Throw an error : can not use "list" as dict as a dict key unhashable type: 'list'


# Keys should of immutable datatype
# mutable vs immutable
# mutable -> can be altered ex: 'List , dictonaries' -> Hence List can,t be KEY
# immutable -> can't be altered ex:'Strings, Tuples' -> Hence Strings and Tuples can be a KEYS

my_dict = {"a": 1, "b": 3, 3: True}
print(my_dict["a"], my_dict.get(3))

my_dict["a"] = 12 # Original dictonary is altered
print(my_dict) 
# hENCE dictonary is a mutable datatype 

print(dir(my_dict))


""""
['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

"""

print(my_dict.items()) # Output is list of Tuples with key and vslues as each element
print(my_dict.keys()) # Returns keys as a list 
print(my_dict.values()) # Returns values as a list