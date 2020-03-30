#!/usr/bin/python

variable = 'tutsplus'

def scopeInvestigator():
    global variable
    variable = 'envato'
    print "the variable insed the function is", variable

scopeInvestigator()
print "the variable insed the function is", variable


def factorial(number):
    if number == 1:
        return 1
    else:
        return number*factorial(number-1)

print factorial(5)
