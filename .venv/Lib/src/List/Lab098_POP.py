squares=[1,4,9,16,25,36,49,64]
print(squares)
print(type(squares))
print(squares.pop()) #remove and return item at index(default last)
print(squares.pop(1))
print(squares)

squares.clear()
print(squares)

#Index(element, start, end)
#Return the index of the first occurence of the element.

number=[10,20,30,40]
print(number.index(30))

print(number.count(30))

number.sort(reverse=True)
print(number)

#reverse()--reverse the list in place
number.reverse()
print(number)

#max(0/ min()/ sum() works for numerical lists.
print(max(number))
print(min(number))
print(sum(number))

#Slicing
print(number)
print(number[1:4])
print(number[-1]) #last element

print("apple" in number)
print(20 in number)

#list creatuin and comprehension
#range(1,5)--> list
l=list(range(1,5))
print(l)

#Nested list
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
print(matrix[1][1])

#del statement--Dleetes an element by index or the whole list.
del number[1]
print(number)