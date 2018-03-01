import textwrap
from text_1 import *
from functions_1 import *
import re
import sys
count = 0
for line in open('text_test.txt', 'r'):
    print line
    if "[c]" in line:
        count+=1

print count
v=raw_input("")
