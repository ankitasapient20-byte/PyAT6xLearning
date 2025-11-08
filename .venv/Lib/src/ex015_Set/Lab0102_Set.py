#SET
#collection of unique
#{}

list_of_unique_items={1,1,2,3,4,4,5,5}
print(list_of_unique_items)

t=("TheTestingAcademy","for","TheTestingAcademy")
print(t)
print(set(t))

mixed={1,"QA",False,3.5}
print(mixed)

empty=set()
print(type(empty))

for item in mixed:
    print(item)

    mixed.add(10)
    print(mixed)
    mixed.remove(10)
    print(mixed)