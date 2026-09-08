# loops in python
# for loop and while loop

# print values from 1 to 10
# if the value is equals to 5, don't print

# count = 0
# while count < 10:
#     count = count + 1
#     if count == 5:
#         continue
#     if count == 7:
#         break
#     print(count)



# For loop

sample  = ["server1", "server2", "server3", "server4"]


# membership operator: 'in'

# value = "server2" in sample
# print(value)



# Use case 1: print all elements inside the list
# for val in sample:
#     print(val)


# Use case 2: print all elements inside a list along with its index
# Enumarate, range
# print(list(enumerate(sample)))
# for idx, value in (enumerate(sample)):
#     print(idx, value)


# range 
# print(list(range(1, 10, 2))) #print all the odd numbers starting from 1 till 10 (not included END INDEX not consider )

# for idx in range(len(sample)):
#     print(idx, sample[idx])


#Tuple unpacking
a, b = (1, 2)
print(a, b)
