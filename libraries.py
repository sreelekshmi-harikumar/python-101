#piece of code we can reuse in our program 
#module - has one or more functions
import random #gives access to all the functions in random module

print(random.choice(["head","tail"]))#gives each option an equal opportunity

print(random.randint(1,10))#gives from 1 to 10, including them

cards = ["jack","queen","king"]
random.shuffle(cards)
print(cards)

import statistics

print(statistics.mean([100,90]))

from sys import argv,exit #it stands for argument vector

print("hello, my name is ",argv[1]) #argv[0] gives filename
#argv[1] gives the name of the command line we enter
#IndexError:When we try to access values that are not present at that position

try:
    print("hello, ",argv[1])
except IndexError:
    print("Too few arguments")

#if we do " " it will be taken as one word on the cml
'''
if len(argv) < 2:
    exit("Less arguments")
elif len(argv)>2:
    exit("Too much arguments")

print("hello ,",argv[1])
'''

#slicing list
for name in argv[1:]:
    print(name)

#PyPI - it is a site where you get python packages
#cowsay - cow says smtg on your screen
#pip is a package manager used to install packages

import cowsay

cowsay.cow("hi my name is",argv[1])

