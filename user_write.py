import textwrap
from text_1 import *
from functions_1 import *
import re

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
