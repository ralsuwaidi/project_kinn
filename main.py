import textwrap
from text_1 import *
from functions_1 import *
from story import *
import re
import os

print "Enter/Paste your content. Ctrl-D to save it."
contents = []
while True:
    try:
        line = raw_input("")
    except EOFError:
        break
    contents.append(line)

print "you typed:", contents

v=raw_input("")


title="""

 _____   _             _                          ___    _____ _
|  _  |_| |_ _ ___ ___| |_ _ _ ___ ___ ___    ___|  _|  |  |  |_|___ ___
|     | . | | | -_|   |  _| | |  _| -_|_ -|  | . |  _|  |    -| |   |   |
|__|__|___|\_/|___|_|_|_| |___|_| |___|___|  |___|_|    |__|__|_|_|_|_|_|

"""
menu="""
+------------Project Kinn------------+

   1. Start Story
   2. Skip To Section
   3. Info

+------------------------------------+

"""
print menu

#Force user to choose
while True:
    try:
        ans = int(raw_input("Enter choice 1, 2 or 3:"))
        if not (1 <= ans <= 3):
            raise ValueError()
    except ValueError:
        print "Invalid Option, you needed to type a 1, 2 or 3...."
    else:
        break

#depending on the choice do these
if ans==1:
    print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    print title
    all_story()
elif ans==2:
    skip_to=raw_input("Where do you want to skip to?\n Type: the name of the section\nArthur\n ...")
    skip_to_story(skip_to)
elif ans==3:
    print "Im About"
else:
    print "Ok now you have to restart the program cuz i didnt think you would choose something else u genius"

raw_input("END")
