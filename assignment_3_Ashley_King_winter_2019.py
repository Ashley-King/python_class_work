'''
    Assignment: 3 - Lists, Loops & Nested Lists
    Author: Ashley King
    Date: 2019-01-28
    Description: Demonstration of basic list methods & loops
'''

# Part 1: Print API names of the List class
print("Output of dir(list):")
dir_list = dir(list)
for item in dir_list:
    print item

# Part 2: Given two lists, create a third list that contains only the common
# elements
list_one = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_two = b = [1, 2, 3, 4, 5, 6, 8, 7, 5, 9, 10, 11, 34, 12, 13]
new_list = []
print("\n")
for element in list_one:
    if list_two.count(element) > 0:
        if new_list.count(element) == 0:
            new_list.append(element)

print ("The common elements are: " + str(new_list) + "\n")

# Part 3: Loop through a nested list
movies = [[["A Dog's Purpose"], ["Buddie", "Margot Robbie", "Carrie Fisher"]],
          [["Star Wars"], ["Harrison Ford", "Carrie Fisher", "Mark Hamill"]],
          [["I Am Legend"], ["Kona", "Will Smith", "Carrie Fisher"]],
          [["Suicide Squad"], ["Viola Davis", "Margot Robbie", "Will Smith"]]]

# print the titles of all movies that Carrie Fisher is in
carrie_movies = []
for movie in movies:
    if movie[1].count("Carrie Fisher") > 0:
        carrie_movies.append(movie[0])

print("The movies that feature Carrie Fisher: ")
for title in carrie_movies:
    print title

# print movies that do not feature Viola Davis
no_viola = []
for movie in movies:
    if movie[1].count("Viola Davis") == 0:
        no_viola.append(movie[0])
print("\n")
print("The movies that do not feature Viola Davis: ")
for title in no_viola:
    print title

# print movies that contain Margot Robbie but not Carrie Fisher
no_carrie = []
for movie in movies:
    if movie[1].count("Margot Robbie") > 0:
        if movie[1].count("Carrie Fisher") == 0:
            no_carrie.append(movie[0])

print("\n")
print("The movies that feature Margot Robbie, but not Carrie Fisher: ")
for title in no_carrie:
    print title

''' ------------------- Run of all parts ------------------------
Output of dir(list):
__add__
__class__
__contains__
__delattr__
__delitem__
__delslice__
__doc__
__eq__
__format__
__ge__
__getattribute__
__getitem__
__getslice__
__gt__
__hash__
__iadd__
__imul__
__init__
__iter__
__le__
__len__
__lt__
__mul__
__ne__
__new__
__reduce__
__reduce_ex__
__repr__
__reversed__
__rmul__
__setattr__
__setitem__
__setslice__
__sizeof__
__str__
__subclasshook__
append
count
extend
index
insert
pop
remove
reverse
sort


The common elements are: [1, 2, 3, 5, 8, 13, 34]

The movies that feature Carrie Fisher: 
["A Dog's Purpose"]
['Star Wars']
['I Am Legend']


The movies that do not feature Viola Davis: 
["A Dog's Purpose"]
['Star Wars']
['I Am Legend']


The movies that feature Margot Robbie, but not Carrie Fisher: 
['Suicide Squad']

------------------- Run of all parts ------------------------'''
