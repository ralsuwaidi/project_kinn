#for any import functions
import textwrap
from text_1 import *
from functions_1 import *
import re


'''ans=raw_input("Do you want to skip to a certain point? [y/n]?")
ans=ans.lower()
if ans=="y" or ans=="yes":
    ans=raw_input("Where to?\n Bambi or Arthur?")
    ans=ans.lower()
    choices = {'bambi': bambi(),
    'arthur': arthur()}
    choices.get(ans, 'default')
else:
    cprint(bambi_1)
    choice(c_bambi_1, a_bambi_1)
    choice(c_bambi_2, a_bambi_2)
    cprint(arthur_1)
    choice(c_arthur_1, a_arthur_1)
    cprint(arthur_2)
    cprint(arthur_2_1)'''

"""
def cat():
  print "cat"

def cow():
  print "cow"

lst = [cat, cow]
lst[0]()
results = [f() for f in options] #to print all
(this works =DDDD)"""

cprint(bambi_1)
choice(c_bambi_1, a_bambi_1)
choice(c_bambi_2, a_bambi_2)
cprint(arthur_1)
choice(c_arthur_1, a_arthur_1)
cprint(arthur_2)
cprint(arthur_2_1)


'''```cprint(bambi_1)
choice(c_bambi_1, a_bambi_1)
choice(c_bambi_2, a_bambi_2)
cprint(arthur_1)
choice(c_arthur_1, a_arthur_1)
cprint(arthur_2)
cprint(arthur_2_1)```'''

raw_input("END")
