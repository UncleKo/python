#!/usr/bin/python

cars = ['honda', 'ford', 'dodge', 'chevy', 'honda', 'dodge']
autos = set(cars)

print autos

motorcycles = ['honda', 'harley', 'yamaha', 'bmw', 'harley']
motos = set(motorcycles)

print motos

print motos - autos
print motos | autos
print motos & autos

dict = {'key' : 'value'}
print dict['key']

dict = {'name':'Jesse','location':'Denver','awesome':'yep'}
print dict['name']
print dict['location']

dict['favorite site'] = 'tutsplus'
print dict

del dict['location']
print dict

print dict.keys()
print dict.values()

print 'name' in dict
print 'location' in dict

