'''
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matthew Francis
ID:      180920880    
Email:   fran0880@mylaurier.ca
__updated__ = "2019-02-27"
-------------------------------------------------------
'''
from List_array import List
from Movie_utilities import read_movies

fv = open("movies.txt", "r")
movies_list = read_movies(fv)
l = List()
l2 = List()

print('Is identical:')
print (l.is_identical(l2))
print()

print('Append and prepend:')

i = 0

source1 = List()
source2 = List()

while i < 3:
    l.append(movies_list[i])
    l.prepend(movies_list[i])
    i += 1 

for val in l:
    print(val)


print('Clean:')
l.clean()
print()


print('Remove Front:')
print(l.remove_front())

print()


print('Get:')
retrieved_obj = l.__getitem__(0)
print(retrieved_obj)
print()

print('Remove many:')
l.remove_many(retrieved_obj)
for val in l:
    print(val)
print()

print('Union:')
a = 3
while a < 5:
    source1.append(movies_list[a])
    a += 1 
    
b = 5 
while b < 7:
    source2.append(movies_list[b])
    b += 1

l.intersection(source1, source2)

for val in l:
    print(val)
print()

print('Union:')
c = 7

while c < 9:
    source1.append(movies_list[c])
    source2.append(movies_list[c])
    c += 1
l.union(source1, source2)

for val in l:
    print(val)
print()

print('Combine:')
d = 9 
while d < 11:
    source1.append(movies_list[c])
    source2.append(movies_list[c])
    d += 1
l.combine(source1, source2)
for val in l:
    print(val)
print()

print('Split:')
target1, target2 = l.split()

for val in target1:
    print(val)
    
print()

for val in target2:
    print(val)
    
print()

print('Split Alt:')
temp_list = target1
target1, target2 = temp_list.split_alt()

for val in target1:
    print(val)
    
print()

for val in target2:
    print(val)
    
print()