#!/usr/bin/python

# import os
# print dir(os)

# os.chdir('/mnt/c/Users/Ko/Desktop')
# print os.getcwd()
# 
# os.makedirs('dir created from python!')

# os.system("sudo apt-get update")


# import sys
# 
# print sys.argv
# # ./09_modules.py argument1

# from sys import argv
# 
# print argv
# # ./09_modules.py argument1
# 
# if argv[-1] == "purr":
#     print "meow!"
# if argv[-2] == "bark":
#     print "ruff!"
# # ./09_modules.py purr


import re #regular expression

print re.search('a', 'apple').group()
print re.search('a(.*)e', 'apple').group()
print re.search('a(.*)e', 'apple').group(1)

print re.findall('\w+@\w+\.com','emai1 is ktee55@gmail.com and email2 is info@shrewd.com')
