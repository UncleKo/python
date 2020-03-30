#!/usr/bin/python

languages = ['python', 'java', 'C++', 'PHP']

for language in languages:
    print language, "rocks!"

dict = {"name":"jesse", "location":"Denver","favorite site":"tutsplus"}

for key in dict:
    print "His", key, "is", dict[key] 

print range(10)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
 
for int in range(10):
    print "int=", int

count = 0
while count < 10:
    print count, "is less than 10"
    count +=1

for i in range(10):
    print "i =", i
    if i == 5:
        break
print "done looping"

for i in range(3):
    print "this is before continue"
    if(i<2): 
        continue
    print "this is after the continue statement"

# it did nothing; but without pass it throws an error!!
for i in range(2):
    pass 


