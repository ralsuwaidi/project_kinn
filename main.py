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

def skip_to_story(x):
  if x.lower()=="arthur":
    arthur()
  elif x.lower()=="bambi":
    bambi()
    arthur()

ans=raw_input("Do you want to skip to a specific story? \n[y,n]\n\n")
if ans=="n":
    print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    print title
    all_story()
else:
    skip_to=raw_input("Where do you want to skip to?\n Type: Arthur or ...")
skip_to_story(skip_to)

raw_input("END")
