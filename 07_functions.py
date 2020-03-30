#!/usr/bin/python

def madlib(adjective='thirsty',name='adam'):
    print "the %s %s ate all the pizza" % (adjective,name)
    # print "the", adjective, name, "ate all the pizza"
    # print ("the {} {} ate all the pizza".format(adjective,name))
    # # python3.6
    # print (f"the {adjective} {name} ate all the pizza")

madlib('hungry','scott')
# madlib(adjective='hungry',name='scott')
# madlib(name='scott')


def shoppingCart(itemName, *avgPrices):
    # print avgPrices #(100,120,34) -> a tuple
    for price in avgPrices:
        print 'price', price

shoppingCart('computer',100,120,34)


def shoppingCart(itemName, **avgPrices):
    # print avgPrices 
    # #{'amazon': 100, 'bestBuy': 34, 'ebay': 120} -> a dictionary
    for shopName in avgPrices:
        print shopName, 'price: ', avgPrices[shopName]

shoppingCart('computer',amazon=100,ebay=120,bestBuy=34)


def shoppingCart(itemName, avgPrices):
    print 'item: ', itemName
    for shopName in avgPrices:
        print shopName, 'price: ', avgPrices[shopName]

def dbLookup():
    dict = {}
    dict['amazon'] = 100
    dict['ebay'] = 120
    dict['bestBuy'] = 34
    return dict

print dbLookup()

shoppingCart('computer', dbLookup())
