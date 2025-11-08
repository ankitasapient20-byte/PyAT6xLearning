my_list=[1,2,3,4,5]
my_list[0]="Ankita"
my_list[1]="Bob"
my_list[2]="Jim"

print(my_list)

for item in my_list:
    print(item)

    #range() this also return the list

    for i in range(1,5):
        print(i)

        my_list=[1,2,3]
    #Indexing
    print("element at index 0-", my_list[0])
    print("element at index 1-", my_list[1])
    print("element at index 2-", my_list[2])

    #append()--#Append obj to the end of the list
    my_list.append(4)
    print(my_list)

    my_list.append(5)
    print(my_list)

    #extend()---Append a new list
    my_list.extend([6,7,8,9])
    print(my_list)

    #insert()
    my_list.insert(1,"Ankita")
    print(my_list)
    print(len(my_list))

    my_list[1]="Mayank"
    print(my_list)

    #remove()
    my_list.remove("Mayank")
    print(my_list)

    my_copy_list=my_list.copy()
    print(my_list)
    print(my_copy_list)

