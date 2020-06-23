'''
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matthew Francis
ID:      180920880    
Email:   fran0880@mylaurier.ca
__updated__ = "2019-03-07"
-------------------------------------------------------
'''
from Sorted_List_linked import Sorted_List
from Movie_utilities import read_movies
fv = open("movies.txt", "r")
movies_list = read_movies(fv)
l = Sorted_List()
l2 = Sorted_List()

print('Is identical:')
print (l.is_identical(l2))
print()


i = 0

source1 = Sorted_List()
source2 = Sorted_List()

while i < 3:
    l.insert(movies_list[i])
    l.insert(movies_list[i])
    i += 1 

for val in l:
    print(val)


print('Max:')
l.max()
print()

print('Min:')
l.min()
print()


print('Remove Front:')
print(l.remove_front())

print()

l.peek()

print('Get:')
retrieved_obj = l.__getitem__(0)
print(retrieved_obj)
print()

print('Remove many:')
l.remove_many(retrieved_obj)
for val in l:
    print(val)
print()

print('Intersection:')
a = 3
while a < 5:
    source1.insert(movies_list[a])
    a += 1 
    
b = 5 
while b < 7:
    source2.insert(movies_list[b])
    b += 1

l.intersection(source1, source2)

for val in l:
    print(val)
print()

print('Union:')
c = 7

while c < 9:
    source1.insert(movies_list[c])
    source2.insert(movies_list[c])
    c += 1
l.union(source1, source2)

for val in l:
    print(val)
print()
print('Clean:')
l.clean()
print()
d = 9 
while d < 11:
    source1.insert(movies_list[c])
    source2.insert(movies_list[c])
    d += 1
for val in l:
    print(val)
print()
source1.remove(movies_list[0])
