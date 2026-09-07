sample = set()
print(sample,type(sample))

#A set consists of unique values only and get unordred collections -> there is no order gurantee in
# beacause of this a set does not supports index
sample = {'a', 'b', 'b', 'c', 'c'}
print(sample)
# print(dir(sample))

"""
[ 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
"""
# print(sample[0]) # throw the error 'set' object is not subscriptable


