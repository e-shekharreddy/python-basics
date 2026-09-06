# List is a Herterogenous
fruits = ["apple", "mango", "orange", "banana", 2, 3, 5, True]

# print(fruits[0:2])
# print(len(fruits))
# print(dir(fruits))

'''
['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'] 

'''

fruits1 = fruits.append(3)
print(fruits, fruits1)

# Iterable Something you can iterate on
# 'int' object is not iterable
# fruits.extend(3) throws an eeror

fruits.extend("3")
print(fruits)


fruits = ["apple", "mango", "orange", "banana", 2, 3, 5, True]

fruits.append(["apple", "mango", "orange", "banana"])
print(fruits)

# output: ['apple', 'mango', 'orange', 'banana', 2, 3, 5, True, ['apple', 'mango', 'orange', 'banana']]

fruits.extend(["apple", "mango", "orange", "banana"])
# print(fruits)

# output: ['apple', 'mango', 'orange', 'banana', 2, 3, 5, True, 'apple', 'mango', 'orange', 'banana']


# print(fruits.count("apple"))
orange_index = fruits.index("orange")
# print(orange_index)

# print(fruits[::-1])

sample_str = "welcome back to git"
sample_str_list = list(sample_str) # converting one data type to another datatype

# print(sample_str_list)

sample_str_join = "".join(list(sample_str))
# print(sample_str_join)

sample_list = [1,2,3,4,5,6,7]
# sample_list.sort()
# print(sample_list)

# sort output: [1, 2, 3, 4, 5, 6, 7]

sample_list_sorted = sorted(sample_list)
print(sample_list, sample_list_sorted)

# outpu : [1, 2, 3, 4, 5, 6, 7] [1, 2, 3, 4, 5, 6, 7]


