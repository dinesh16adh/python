set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 3, 8, 5}
# set = set1.union(set2)
# print(set)
# set1.intersection_update(set2)
# print(set1)
# set = set1.intersection(set2)
# print(set)
# set1.symmetric_difference_update(set2)
# print(set1)
set = set1.symmetric_difference(set2)
print(set)
set1.pop()
print(set1)
