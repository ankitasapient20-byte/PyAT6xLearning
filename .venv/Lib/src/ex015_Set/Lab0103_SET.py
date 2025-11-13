a={1,2,3}
b={3,4,5}
print(a | b)
print(a.union(b))

print(a&b)
print(a.intersection(b))

print(a.difference(b))
print(a.symmetric_difference(b))
print(a-b)


set1={1,2,3}
set2={4,5,6}
my_set = set1.union(set2)
print(my_set)

set1={1,2,3,4,5}
set2={4,5,6,7,8}
my_set = set1.intersection(set2)
print(my_set)
