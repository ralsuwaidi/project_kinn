import textwrap
from text_1 import *
from functions_1 import *
import re
import sys


def write_to_file(file_name):
    filename=file_name+".txt"
    count = 0
    for line in open(filename, 'r'):
        print line
        if "[c]" in line:
            count+=1
    print "Write something and save it with CTRL+A then ENTER\n\n"
    lines=[]
    while "^A" not in lines:
        new_line=raw_input("")
        lines.append(new_line)
    print "saving to text done"
    with open(filename, 'a') as f:
        f.writelines("%s\n" % l for l in lines)

v=raw_input("what is the file name?")
write_to_file(v)
v=raw_input("DONE")
