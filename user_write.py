import textwrap, re, sys
from text_1 import *
from functions_1 import *




def write_to_file(name):
    filename="text_test.txt"
    count = 0
    for line in open(filename, 'r'):
        print line
        if "[c]" in line:
            count+=1
    print "If you want to write a text use [t] before the text and if you want to write a choice use [c]\n\n"
    lines=[]
    while "END" not in lines:
        new_line=raw_input("")
        lines.append(new_line)
    print "saving to text done"
    with open(filename, 'a') as f:
        f.writelines("%s\n" % l for l in lines)


v=raw_input("what is the your name?")
write_to_file(v)
v=raw_input("DONE")
