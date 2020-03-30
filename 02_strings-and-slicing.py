#!/usr/bin/python

import sys
print(sys.version_info)

print "Hello World"

var1 = "this is a string"
var2 = " and another"

print var1 + var2

var3 = var1 + var2

# multiline = "This is a \n multiline string"
multiline = "This is a \n\
multiline string"

print multiline

multiline = """this is also
a
multiline string"""

print multiline


print var3

print len(var3)

print var3[0]
print var3[1]
print var3[2]

print var3[-1]
print var3[-2]
print var3[-3]

print var3[1:4]
print var3[1:-6]
print var3[10:]
print var3[:-10]
