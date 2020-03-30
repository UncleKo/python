#!/usr/bin/python

list = ['the', 'holy', 'grail']

print list

nested_list = ['the', 'monty', 'python', 'and', list]

print nested_list

print 'monty' in nested_list

print 'holy' in nested_list

print nested_list[1]

print nested_list[1][1]

print nested_list[-1]

print nested_list[-1][1]

print nested_list[0:2]

print nested_list[2:-2]

nested_list[1] = 'awesome'
print nested_list

# nested_list[1] = ['tuts', 'plus']
# nested_list[-1] = ['tuts', 'plus']
nested_list[-1:] = ['tuts', 'plus']
# nested_list[-2:] = ['tuts', 'plus']
print nested_list

nested_list.append('for sure')
# nested_list.append(['for sure','to be'])
print nested_list

nested_list.insert(1, 'super')
print nested_list

another_list = ['python', 'rocks']
print another_list

nested_list.extend(another_list)
print nested_list

# nested_list.extend(['python', 'rocks'])
# print nested_list

nested_list.remove('awesome')
print nested_list


tuple = 'one', 'two', 'three'
print tuple

print tuple[1]
print tuple[2]
print tuple[:2]
print tuple[1:]

tuple2 = 'tuts','plus'
tuple3 = tuple2,tuple

print tuple3
